
from django.db import models

class TimeStampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Erasable(TimeStampable):
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class Humanifiable(Erasable):
    GENDER_OPTIONS = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    gender = models.CharField(blank=False, choices=GENDER_OPTIONS)
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField()
    id_number = models.PositiveIntegerField(blank=True)


class Describeable(Humanifiable):
    BUILDS = (
        ('tall','Tall'),
        ('petite', 'Petite'),
        ('heavyset', 'Heavyset'),
        ('slim', 'Slim'),
        ('average', 'Average'),
    )

    COMPLEXIONS = (
        ('dark', 'Dark'),
        ('light', 'Light'),
        ('chocolate', 'Chocolate'),
    )

    ETHNICITIES = (
        ('African','African'),
        ('Caucasian', 'Caucasian'),
        ('Asian','Asian'),
        ('Indian', 'Indian'),
        ('Arab', 'Arab'),
    )

   AGE_GROUPS = (
        ('child', 'Child (0-12'),
        ('teen', 'Teen (13-19'),
        ('adult', 'Young Adult (20-32'),
        ('middle-aged', 'Middle Aged Adult (32-49'),
        ('old', 'Old Adult (50+')
    )

    AGE_GROUPS = (
        ('child', 'Child (0-12'),
        ('teen', 'Teen (13-19'),
        ('adult', 'Young Adult (20-32'),
        ('middle-aged', 'Middle Aged Adult (32-49'),
        ('old', 'Old Adult (50+')
    )

    age_group = models.CharField(choices=AGE_GROUPS)
    verbose_description = models.TextField()
    height = models.CharField(null=True)
    complexion = models.CharField(null=True, choices=COMPLEXIONS)
    clothing = models.CharField(null=True)
    ethnicity = models.CharField(choices=ETHNICITIES)
    build = models.CharField(null=True, choices=BUILDS)


class Contactable():
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    alt_phone_no = models.CharField(max_length=15, blank=True, null=True)
    whatsapp_no = models.CharField(max_length=15, black=True, null=True)


class Sociable(Contactable):
    x_handle = models.CharField(max_length=155)
    instagram_handle = models.CharField(max_length=155)
    facebook_hanle = models.CharField(max_length=155)
    tiktok_handle = models.CharField(max_length=155)


class Addressable():
    street = models.CharField(max_length=250, blank=True)
    building = models.CharField(max_length=100)
    floor = models.IntegerField(default=0)
    unit = models.CharField(max_length=50)
    estate = models.CharField(max_length=155, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    physical_address = models.TextField(blank=True, null=True)


class Locatable(Addressable):
    maps_url = models.URLField()
    maps_code = models.CharField()
    longitude = models.CharField(max_length=75)
    latitude = models.CharField(max_length=75)
