from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Provider, Medication, Prescription, Appointment


class MedicationForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    instructions = forms.CharField(max_length=512, required=False)
    recommended_dose = forms.CharField(max_length=50, required=True)


class PatientRegistrationForm(UserCreationForm):
    age = forms.IntegerField(required=True)
    provider = forms.ModelChoiceField(queryset=Provider.objects.all(), required=False)
    birthdate = forms.DateField(required=True)
    allergies = forms.CharField(max_length=128)


class ProviderRegistrationForm(UserCreationForm):
    patient = forms.ModelMultipleChoiceField(queryset=Patient.objects.all(), required=False)
    phone_number = forms.CharField(max_length=14)

    
class PerscriptionForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), required=True)
    medication = forms.ModelChoiceField(queryset=Medication.objects.all(), required=True)
    date_prescribed = forms.DateTimeField(required=True)
    expiration = forms.DateField(required=True)
    dose = forms.CharField(max_length=50, required=True)


class AppointmentForm(forms.Form):
    date_time = forms.DateTimeField(required=True)
    duration = forms.TimeField(required=True)
    provider = forms.ModelChoiceField(queryset=Provider.objects.all(), required=True)
    note = forms.CharField(widget=forms.Textarea)
