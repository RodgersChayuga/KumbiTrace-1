# Generated by Django 5.0.7 on 2024-07-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumbitraceweb', '0003_missingperson_tip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
