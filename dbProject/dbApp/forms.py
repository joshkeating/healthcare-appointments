from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Provider, Medication, Prescription, Appointment
from datetimewidget.widgets import DateTimeWidget


TIME_CHOICES = (
                    ('07:00:00', '7 AM'),
                    ('08:00:00', '8 AM'),
                    ('09:00:00', '9 AM'),
                    ('10:00:00', '10 AM'),
                    ('11:00:00', '11 AM'),
                    ('12:00:00', 'Noon'),
                    ('13:00:00', '1 PM'),
                    ('14:00:00', '2 PM'),
                    ('15:00:00', '3 PM'),
                    ('16:00:00', '4 PM'),
                    ('17:00:00', '5 PM'),
                )

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
    time = forms.ChoiceField(required=True, widget=forms.Select, choices=TIME_CHOICES)
    duration = forms.DecimalField(required=True, max_digits=2, decimal_places=1)
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), required=True)
    note = forms.CharField(widget=forms.Textarea)



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())




