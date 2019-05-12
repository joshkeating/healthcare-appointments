from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Medication, Prescription, Admin, Appointment
from .serializers import MedicationSerializer, PrescriptionSerializer, AdminSerializer, AppointmentSerializer
from .forms import MedicationForm, PatientRegistrationForm, PerscriptionForm, AppointmentForm
from django.contrib import messages


from django.http import JsonResponse
from django.http import HttpResponse


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
            medication = Medication(
                name=name, instructions=instructions, recommended_dose=recommended_dose)
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


class PrescriptionAPI(APIView):

	def get(self, request, format=None):

		if request.user.has_perm('dbApp.view_perscriptions'):
				prescriptions = Prescription.objects.all()
				serializer = PrescriptionSerializer(prescriptions, many=True)
				return JsonResponse(serializer.data, safe=False, status=200)
		else:
			return HttpResponse("User is not authorized", status=401)


	def post(self, request, format=None):

		if request.user.has_perm('dbApp.add_perscriptions'):

			form = PerscriptionForm(request.POST)

			if form.is_valid():
				patient = form.cleaned_data["patient"]
				medication = form.cleaned_data["medication"]
				date_prescribed = form.cleaned_data["date_prescribed"]
				expiration = form.cleaned_data["expiration"]
				dose = form.cleaned_data["dose"]
				prescription = Prescription(
				    patient=patient, medication=medication, date_prescribed=date_prescribed, expiration=expiration, dose=dose)
				prescription.save()
				return Response(status=status.HTTP_201_CREATED)

		else:
			return HttpResponse("User is not authorized", status=401)


	def patch(self, request, format=None):
		id = request.data["id"]
		patient = request.data["patient"]
		medication = request.data["medication"]
		date_prescribed = request.data["date_prescribed"]
		expiration = request.data["expiration"]
		dose = request.data["dose"]

		prescription = Prescription.objects.get(id=id)
		prescription.patient = patient
		prescription.medication = medication
		prescription.date_prescribed = date_prescribed
		prescription.expiration = expiration
		prescription.dose = dose
		prescription.save()
		serialized_prescription = PrescriptionSerializer(prescription)
		return Response(serialized_prescription.data)


class AdminAPI(APIView):
	'''TODO: more HTTP methods'''

	def get(self, request, format=None):
		'''show all current admins in the system'''

		if request.user.has_perm('dbApp.view_admins'):

			admins = Admin.objects.all()
			serializer = AdminSerializer(admins, many=True)
			return JsonResponse(serializer.data, safe=False, status=200)

		else:
			return HttpResponse("User is not authorized", status=401)



class AppointmentAPI(APIView):

    def get(self, request, format=None):
        '''get appointments for current user'''
        appointment = Appointment.objects.get(patient=request.user.id)
        serialized_appointment = AppointmentSerializer(appointment)
        return Response(serialized_appointment.data)
	

    def post(self, request, format=None):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            date_time = form.cleaned_data["date_time"]
            duration = form.cleaned_data["duration"]
            patient = request.user.id
            provider = form.cleaned_data["provider"]
            note = form.cleaned_data["note"]
            appointment = Appointment(
                date_time=date_time, duration=duration, patient=patient, provider=provider, note=note)
            appointment.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        id = request.data["id"]
        date_time = request.data["date_time"]
        duration = request.data["duration"]
        patient = request.data["patient"]
        provider = request.data["provider"]
        note = request.data["note"]

        appointment = Appointment.objects.get(id=id)
        appointment.date_time = date_time
        appointment.duration = duration
        appointment.patient = patient
        appointment.provider = provider
        appointment.note = note
        appointment.save()
        serialized_appointment = AppointmentSerializer(appointment)
        return Response(serialized_appointment.data)
