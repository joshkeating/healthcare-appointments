from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AdminUser(AbstractUser):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(AdminUser, self).save(*args, **kwargs)


class Prescription(models.Model):

    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', models.SET_NULL)
    medication = models.ForeignKey('Medication', models.SET_NULL)
    date_prescribed = models.DateTimeField()
    expiration = models.DateField()
    dose = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Prescription, self).save(*args, **kwargs)


class Medication(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    instructions = models.CharField(max_length=30)
    recommended_dose = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Medication, self).save(*args, **kwargs)