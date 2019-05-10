from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):

    class Meta:
        permissions = [
            ("view_perscriptions", "View all prescriptions in the database"),
            ("add_perscriptions", "Add prescription to the database"),
            ("edit_medication", "Add or remove medications"),
        ]

    def save(self, *args, **kwargs):
        super(Admin, self).save(*args, **kwargs)


class Prescription(models.Model):

    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', null=True, on_delete=models.SET_NULL)
    medication = models.ForeignKey('Medication', null=True, on_delete=models.SET_NULL)
    date_prescribed = models.DateTimeField()
    expiration = models.DateField()
    dose = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Prescription, self).save(*args, **kwargs)


class Medication(models.Model):
    name = models.CharField(max_length=30, unique=True)
    instructions = models.CharField(max_length=30)
    recommended_dose = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Medication, self).save(*args, **kwargs)

    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    age = models.SmallIntegerField()
    allergies = models.CharField(blank=True, default='', max_length=128)
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, null=True), 
    prescriptions = models.ManyToManyField('Prescription', related_name='patient_prescriptions')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)
    patients = models.ManyToManyField('Patient', related_name='provider_patients')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Appointment(models.Model):
    date_time = models.DateTimeField()
    duration = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, related_name='appointment_patient')
    provider = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, related_name='appointment_provider')
    note = models.CharField(blank=True, default='', max_length=1024)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
