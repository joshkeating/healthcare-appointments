from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Provider


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