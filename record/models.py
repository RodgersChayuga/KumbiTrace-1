import uuid
from django.db import models
from django.contrib.auth.models import User
from media.models import Media

# Create your models here.
class Record(models.Model):
    STATUS = (
        ('new','New'),
        ('processing', 'Validation in Progress'),
        ('pending', 'Validation Pending'),
        ('missing', 'Missing'),
        ('found', 'Found & Free'),
        ('deceased', 'Deceased'),
        ('arrested', 'Confirmed Arrested'),
    )

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    first_name = models.CharField(min_length=3, max_length=25, blank=False)
    last_name = models.CharField(min_length=3, max_length=25, blank=False)
    nickname = models.CharField(min_length=3, max_length=100, blank=True)

    seen_county = models.ForeignKey("County", on_delete=RESTRICT, null=False)
    seen_location = models.CharField(min_length=3, max_length=255)
    seen_date = models.DateField()
    seen_time = models.TimeField()
    seen_dressing = models.TextField()
    reported_by = models.ForeignKey("User",
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    verified_by = models.ForeignKey("User",
                                    on_delete=models.CASCADE,
                                    blank=True
                                    null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone_no = models.CharField(min_length=9,max_length=12)
    alt_phone_no = models.CharField(min_length=9,max_length=12)
    email_address = models.EmailField()
    residential_address = models.TextField()
    county_id = models.ForeignKey("County", on_delete=RESTRICT, null=False)
    duration = models.DurationField()



class County(models.Model):
    id = models.IntegerField()
    name = models.CharField()

    def __str__(self):
        return self.value

class RecordUpdates(models.Model):
    id = models.AutoField()
    created = models.DateTimeField(auto_now_add=True)
    person_id = models.ForeignKey("User",
                                    on_delete=models.RESTRICT,
                                    blank=True,
                                    null=True)

    updated_by = models.ForeignKey("User",
                                    on_delete=models.RESTRICT,
                                    blank=True,
                                    null=True)



class Media(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    record_id = models.ForeignKey("Record", on_delete=CASCADE, blank=False)
    filename = models.CharField(max_length=225)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

class Reporter(models.Model):
    STATUS = (
        ('registered', 'Registered'),
        ('unregistered', 'Unregistered'),
    )

    user_id = models.ForeignKey("Users", on_delete=RESTRICT, null=True)
    full_name = models.CharField(min_length=3, max_length=25)
    phone_number = models.CharField(min_length=9, max_length=12)
    email_address = models.EmailField(max_length=50)
    relationship_id = models.ForeignKey("Relationships", on_delete=RESTRICT, blank=False)
    created = models.DateTimeField()
    status = models.BooleanField(default=True)

class Relationships(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add_add=True)
    created_by = models.ForeignKey("User", on_delete=RESTRICT, null=False)
    status = models.BooleanField(default=True)

class Comments(models.Model):
    id = model.IntegerField(primary_key=True)
    parent_id = models.ForeignKey(self, on_delete=RESTRICT, null=True)
    record_id = models.ForeignKey("Record", on_delete=RESTRICT, null=True)
    user_id = models.ForeignKey("User", on_delete=RESTRICT, null=True)
    comment = models.TextField(min_length=10)
    created = models.DateTimeField()
    status = models.BooleanField(default=True)

    def clean(self):
        if len(self.comment) > 10000:
            raise ValidationError('Comment is too long!')






