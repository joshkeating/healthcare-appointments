from django.db import models
from django.contrib.auth.models import AbstractUser


class Patient(AbstractUser):
    first_name = models.CharField(required=True, max_length=30)
    last_name = models.CharField(required=True, max_length=30)
    birthdate = models.DateField(required=True)
    age = models.SmallIntegerField(required=True)
    allergies = models.CharField(blank=True, default='')
    provider = models.ForeignKey(Provider, required=True, on_delete=models.SET_NULL)
    prescriptions = models.ManyToManyField(Prescription, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Provider(AbstractUser):
    first_name = models.CharField(required=True, max_length=30)
    last_name = models.CharField(required=True, max_length=30)
    phone_number = models.CharField(required=True, max_length=14)
    patients = models.ManyToManyField(Patient, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Appointment(models.Model):
    date_time = models.DateTimeField(required=True)
    duration = models.TimeField(required=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, required=True)
    provider = models.ForeignKey(Patient, on_delete=models.SET_NULL, required=True)
    note = models.CharField(blank=True, default='', max_length=1024)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)