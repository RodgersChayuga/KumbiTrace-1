
from django.db import models

class TimeStampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Erasable(TimeStampable):
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Contactable(Erasable):
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    alt_phone_no = models.CharField(max_length=15, blank=True, null=True)
    physical_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True

class Locatable(Contactable):
    physical_address = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=225)
    city = models.CharField(max_length=100, blank=True, null=True)
    county = models.IntegerField(blank=True, null=True)
