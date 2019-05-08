from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AdminUser(AbstractUser):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, required=True)
    first_name = models.CharField(max_length=30, required=True)
    last_name = models.CharField(max_length=30, required=True)
    email = models.EmailField(max_length=254, required=True)
    is_staff = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(AdminUser, self).save(*args, **kwargs)


class Prescription(models.Model):

    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', models.SET_NULL)
    medication = models.ForeignKey('Medication', models.SET_NULL)
    date_prescribed = models.DateTimeField(required=True)
    expiration = models.DateField(required=True)
    dose = models.CharField(max_length=30, required=True)

    def save(self, *args, **kwargs):
        super(Prescription, self).save(*args, **kwargs)


class Medication(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True, required=True)
    instructions = models.CharField(max_length=30, required=True)
    recommended_dose = models.CharField(max_length=30, required=True)

    def save(self, *args, **kwargs):
        super(Medication, self).save(*args, **kwargs)