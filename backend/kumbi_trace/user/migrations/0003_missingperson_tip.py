# Generated by Django 5.0.7 on 2024-07-16 04:38

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumbitraceweb', '0002_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissingPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('last_seen_date', models.DateField()),
                ('last_seen_location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='missing_persons/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('found', 'Found'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('date_reported', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('contact_person_type', models.CharField(choices=[('relative', 'Relative'), ('friend', 'Friend'), ('concerned_citizen', 'Concerned Citizen')], max_length=20)),
                ('contact_person_phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+254XXXXXXXXX' or '07XXXXXXXX' or '01XXXXXXXX'. Up to 13 digits allowed.", regex='^(?:\\+254|0)[17]\\d{8}$')])),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('ip_address', models.GenericIPAddressField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('missing_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tips', to='kumbitraceweb.missingperson')),
                ('submitted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
