from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import RegexValidator, \
    MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
import pytz
from django.conf import settings


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)

    # Override related_name for groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='''The groups this user belongs to. A user will get all
                    permissions granted to each of their groups.''',
        related_name='customuser_set',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username


class MissingPerson(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('found', 'Found'),
        ('rejected', 'Rejected'),
    ]

    CONTACT_PERSON_CHOICES = [
        ('relative', 'Relative'),
        ('friend', 'Friend'),
        ('concerned_citizen', 'Concerned Citizen'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    case_number = models.IntegerField(unique=True, validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    last_seen_date = models.DateField()
    last_seen_location = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='missing_persons/', blank=False, null=False)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_reported = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    contact_person_type = models.CharField(max_length=20, choices=CONTACT_PERSON_CHOICES)
    contact_person_phone = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex=r'^(?:\+254|0)[17]\d{8}$',
            message="Phone number must be entered in the format: '+254XXXXXXXXX' or '07XXXXXXXX' or '01XXXXXXXX'. Up to 13 digits allowed."
        ),
    ])

    def __str__(self):
        return f"Case {self.case_number}: {self.name} - {self.get_status_display()}"

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set the timezone for new instances
            nairobi_tz = pytz.timezone('Africa/Nairobi')
            self.date_reported = timezone.now().astimezone(nairobi_tz)
        super().save(*args, **kwargs)

@receiver(pre_save, sender=MissingPerson)
def assign_case_number(sender, instance, **kwargs):
    if not instance.case_number:
        last_case = MissingPerson.objects.order_by('-case_number').first()
        if last_case:
            new_case_number = last_case.case_number + 1
        else:
            new_case_number = 1000

        # Ensure the case number is within the valid range
        if new_case_number > 9999:
            new_case_number = 1000

        instance.case_number = new_case_number

class Tip(models.Model):
    missing_person = models.ForeignKey(MissingPerson, on_delete=models.CASCADE, related_name='tips')
    content = models.TextField()
    submitted_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f"Tip for Case {self.missing_person.case_number} - {self.date_submitted}"
