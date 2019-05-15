from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Provider, Medication, Prescription, Appointment


TIME_CHOICES = (('00:00:00', 'Midnight'),
                    ('01:00:00', '01 AM'),
                    ('02:00:00', '02 AM'),
                    ('03:00:00', '03 AM'),
                    ('04:00:00', '04 AM'),
                    ('05:00:00', '05 AM'),
                    ('06:00:00', '06 AM'),
                    ('07:00:00', '07 AM'),
                    ('08:00:00', '08 AM'),
                    ('09:00:00', '09 AM'),
                    ('10:00:00', '10 AM'),
                    ('11:00:00', '11 AM'),
                    ('12:00:00', 'Noon'),
                    ('13:00:00', '01 PM'),
                    ('14:00:00', '02 PM'),
                    ('15:00:00', '03 PM'),
                    ('16:00:00', '04 PM'),
                    ('17:00:00', '05 PM'),
                    ('18:00:00', '06 PM'),
                    ('19:00:00', '07 PM'),
                    ('20:00:00', '08 PM'),
                    ('21:00:00', '09 PM'),
                    ('22:00:00', '10 PM'),
                    ('23:00:00', '11 PM'), )

class MedicationForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    instructions = forms.CharField(max_length=512, required=False)
    recommended_dose = forms.CharField(max_length=50, required=True)


class PatientRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=30)
    age = forms.IntegerField(required=True)
    provider = forms.ModelChoiceField(queryset=Provider.objects.all(), required=False)
    birthdate = forms.DateField(required=True)
    allergies = forms.CharField(max_length=128)


class ProviderRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(max_length=50)
    patients = forms.ModelMultipleChoiceField(queryset=Patient.objects.all(), required=False)
    phone_number = forms.CharField(max_length=14)


class PrescriptionForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), required=True)
    medication = forms.ModelChoiceField(queryset=Medication.objects.all(), required=True)
    date_prescribed = forms.DateField(required=True, widget=forms.SelectDateWidget)
    expiration = forms.DateField(required=True, widget=forms.SelectDateWidget)
    dose = forms.CharField(max_length=50, required=True)


class AppointmentForm(forms.Form):
    date = forms.DateField(required=True, widget=forms.SelectDateWidget)
    time = forms.ChoiceField(required=True, choices=TIME_CHOICES)
    duration = forms.DecimalField(required=True, max_digits=2, decimal_places=1)
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), required=True)
    note = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())