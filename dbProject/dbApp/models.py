from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):

    is_admin = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # assign custom permissions to this user type
    class Meta:
        permissions = [
            ("view_perscriptions", "View all prescriptions in the database"),
            ("add_perscriptions", "Add prescription to the database"),
            ("edit_medication", "Add or remove medications"),
            ("view_admins", "View all admins in the database"),
        ]

    def save(self, *args, **kwargs):
        super(Admin, self).save(*args, **kwargs)


class Prescription(models.Model):

    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', null=True, on_delete=models.SET_NULL)
    medication = models.ForeignKey('Medication', null=True, on_delete=models.SET_NULL)
    date_prescribed = models.DateField()
    expiration = models.DateField()
    dose = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Prescription, self).save(*args, **kwargs)

    def __str__(self):
        if self.patient is None:
            return 'Prescription ' + str(self.id)
        return 'Prescription for ' + self.patient.user.first_name + ' on ' + str(self.date_prescribed)


class Medication(models.Model):
    name = models.CharField(max_length=30, unique=True)
    instructions = models.CharField(max_length=30)
    recommended_dose = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Medication, self).save(*args, **kwargs)

    def __str__(self):
        if self.name is '':
            return 'Medication ' + str(self.id)
        return self.name

    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    age = models.SmallIntegerField()
    allergies = models.CharField(blank=True, default='', max_length=128)
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, null=True, related_name='provider_patient')
    prescriptions = models.ManyToManyField('Prescription', related_name='patient_prescriptions', blank=True)

    def get_full_name(self):
        if self.user.first_name is '':
            return 'Patient ' + str(self.id)
        return self.user.first_name + " " + self.user.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)
    patients = models.ManyToManyField('Patient', related_name='provider_patients')

    def get_full_name(self):
        if self.user.first_name is '':
            return 'Provider ' + str(self.id)
        return self.user.first_name + " " + self.user.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()


class Appointment(models.Model):
    date_time = models.DateTimeField()
    duration = models.DecimalField(max_digits=2, decimal_places=1)
    patient = models.ForeignKey('Patient', on_delete=models.SET_NULL, null=True, related_name='appointment_patient')
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, null=True, related_name='appointment_provider')
    note = models.CharField(blank=True, default='', max_length=1024)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.patient.get_full_name() + ' and ' + self.provider.get_full_name() + ' on ' + str(self.date_time)
