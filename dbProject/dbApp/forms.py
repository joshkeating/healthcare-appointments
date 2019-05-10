from django import forms


class MedicationForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    instructions = forms.CharField(max_length=512, required=False)
    recommended_dose = forms.CharField(max_length=50, required=True)