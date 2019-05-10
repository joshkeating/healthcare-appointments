from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Medication
from .serializers import MedicationSerializer
from .forms import MedicationForm, PatientRegistrationForm
from django.contrib import messages

# Create your views here.

def login(request):

	if request.method == 'POST':

        return
    else:
        return



def register(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
            
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

            # auth and login user
			user = authenticate(username=username, password=password)
            login(request, user)
			
			# redirect here
	else:
		# return the form if no input
		form = UserCreationForm()
	

class MedicationAPI(APIView):

    def get(self, request, format=None):
        """ get all medications """
        medications = Medication.objects.all()
        serialized_medications = MedicationSerializer(medications, many=True)
        return Response(serialized_medications.data)

    def post(self, request, format=None):
        form = MedicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            instructions = form.cleaned_data["instructions"]
            recommended_dose = form.cleaned_data["recommended_dose"]
            medication = Medication(name=name, instructions=instructions, recommended_dose=recommended_dose)
            medication.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


    def patch(self, request, format=None):
        id = request.data["id"]
        name = request.data["name"]
        instructions = request.data["instructions"]
        recommended_dose = request.data["recommended_dose"]
        medication = Medication.objects.get(id=id)
        medication.name = name
        medication.instructions = instructions
        medication.recommended_dose = recommended_dose
        medication.save()
        serialized_medication = MedicationSerializer(medication)
        return Response(serialized_medication.data)
