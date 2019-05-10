from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Admin(models.Model):
    '''
    TODO: This needs to be looked at again, the admin user needs to have some 
    novel functionality
    '''

    # id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=30, required=True)
    # first_name = models.CharField(max_length=30, required=True)
    # last_name = models.CharField(max_length=30, required=True)
    # email = models.EmailField(max_length=254, required=True)
    # is_staff = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(Admin, self).save(*args, **kwargs)


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


class Patient(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    birthdate = models.DateField(required=True)
    age = models.SmallIntegerField()
    allergies = models.CharField(blank=True, default='')
    provider = models.ForeignKey('Provider', required=True, on_delete=models.SET_NULL)
    prescriptions = models.ManyToManyField('Prescription', blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Provider(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    phone_number = models.CharField(required=True, max_length=14)
    patients = models.ManyToManyField('Patient', on_delete=models.SET_NULL)

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
        