from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import CustomUser, MissingPerson, Tip
from django.utils.html import format_html
from django.urls import reverse

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )

@admin.register(MissingPerson)
class MissingPersonAdmin(admin.ModelAdmin):
    list_display = ('case_number', 'name', 'age', 'gender', 'last_seen_date', 'status', 'date_reported', 'admin_actions')
    list_filter = ('status', 'gender', 'date_reported')
    search_fields = ('case_number', 'name', 'description')
    readonly_fields = ('case_number', 'date_reported', 'last_updated')
    actions = ['approve_reports', 'reject_reports', 'mark_as_found']

    fieldsets = (
        ('Case Information', {'fields': ('case_number', 'status')}),
        ('Personal Details', {'fields': ('name', 'age', 'gender', 'photo')}),
        ('Last Seen', {'fields': ('last_seen_date', 'last_seen_location')}),
        ('Description', {'fields': ('description',)}),
        ('Contact Information', {'fields': ('contact_person_type', 'contact_person_phone')}),
        ('Reporter', {'fields': ('reporter',)}),
        ('Dates', {'fields': ('date_reported', 'last_updated')}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('reporter',)
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:
            obj.reporter = request.user
        super().save_model(request, obj, form, change)

    def approve_reports(self, request, queryset):
        queryset.update(status='approved')
    approve_reports.short_description = "Approve selected reports"

    def reject_reports(self, request, queryset):
        queryset.update(status='rejected')
    reject_reports.short_description = "Reject selected reports"

    def mark_as_found(self, request, queryset):
        queryset.update(status='found')
    mark_as_found.short_description = "Mark selected reports as found"

    def admin_actions(self, obj):
        view_tips_url = reverse('admin:kumbitraceweb_tip_changelist') + f'?missing_person__id__exact={obj.id}'
        return format_html(
            '<a class="button" href="{}">View Tips</a>',
            view_tips_url
        )
    admin_actions.short_description = 'Actions'

@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ('missing_person', 'submitted_by', 'is_anonymous', 'date_submitted', 'content_preview')
    list_filter = ('is_anonymous', 'date_submitted', 'missing_person')
    search_fields = ('missing_person__name', 'missing_person__case_number', 'content')
    readonly_fields = ('missing_person', 'submitted_by', 'ip_address', 'date_submitted', 'is_anonymous')

    fieldsets = (
        ('Tip Information', {'fields': ('missing_person', 'content')}),
        ('Submission Details', {'fields': ('submitted_by', 'is_anonymous', 'ip_address', 'date_submitted')}),
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content Preview'

# Unregister the original Group admin
admin.site.unregister(Group)

# Register the new Group admin
admin.site.register(Group, GroupAdmin)