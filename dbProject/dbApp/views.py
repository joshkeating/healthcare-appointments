from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Medication, Prescription, Admin, Appointment, Provider, Patient
from .serializers import MedicationSerializer, PrescriptionSerializer, AdminSerializer, AppointmentSerializer
from .forms import MedicationForm, PatientRegistrationForm, PrescriptionForm, AppointmentForm
from django.contrib import messages
from datetime import datetime
from time import strptime

from django.contrib.auth.decorators import permission_required

from django.http import JsonResponse
from django.http import HttpResponse


class MedicationAPI(APIView):
	
	def get(self, request, format=None):
		""" get all medications """
		try:
			medications = Medication.objects.all()
			serialized_medications = MedicationSerializer(medications, many=True)
			return Response(serialized_medications.data)
		except:
			messages.error('Medications could not be retrieved successfully.')
			return redirect('homepage')

	def post(self, request, format=None):
		form = MedicationForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data["name"]
			instructions = form.cleaned_data["instructions"]
			recommended_dose = form.cleaned_data["recommended_dose"]
			medication = Medication(
				name=name, instructions=instructions, recommended_dose=recommended_dose)
			medication.save()
			messages.success(request, 'Medication added!')
			return redirect('medications')
		return redirect('medications')

	def patch(self, request, format=None):
		try:
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
			return Response(serialized_medication.data, status=status.HTTP_200_OK)
		except:
			return Response('Could not edit medication.', status=status.HTTP_400_BAD_REQUEST)

class PrescriptionAPI(APIView):

	# @permission_required('dbApp.view_perscriptions')
	def get(self, request, format=None):

		if request.user.has_perm('dbApp.view_perscriptions'):
			prescriptions = Prescription.objects.all()
			serializer = PrescriptionSerializer(prescriptions, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response("User is not authorized", status=status.HTTP_401_UNAUTHORIZED)

	# @permission_required('dbApp.add_perscriptions')
	def post(self, request, format=None):
		# accessible to providers, and admins

		# if request.user.has_perm('dbApp.add_perscriptions'):
		form = PrescriptionForm(request.POST)
		if form.is_valid():
			patient = form.cleaned_data["patient"]
			medication = form.cleaned_data["medication"]
			date_prescribed = form.cleaned_data["date_prescribed"]
			expiration = form.cleaned_data["expiration"]
			dose = form.cleaned_data["dose"]
			prescription = Prescription(patient=patient, medication=medication,
										date_prescribed=date_prescribed, expiration=expiration, dose=dose)
			prescription.save()
			patient.prescriptions.add(prescription)
			messages.success(request, 'Prescription added!')
			return redirect('provider_prescription')
		else:
			messages.error(request, 'Invalid entry!')
			return redirect('add_prescription')
		# else:
		# 		messages.error(request, 'User does not have persmissions to access this!')
		# 		return redirect('add_prescription')

	def patch(self, request, format=None):
		try:
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
			return Response(serialized_prescription.data, status=status.HTTP_200_OK)
		except:
			return Response('Could not edit prescription.', status=status.HTTP_400_BAD_REQUEST)


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
			date = form.cleaned_data["date"]
			time_obj = form.cleaned_data["time"]
			date_time = datetime.combine(date, datetime.strptime(time_obj, '%H:%M:%S').time())
			duration = form.cleaned_data["duration"]
			patient = form.cleaned_data["patient"]
			provider = request.user.provider
			note = form.cleaned_data["note"]

			appointment = Appointment(
				date_time=date_time, duration=duration, patient=patient, provider=provider, note=note)
			appointment.save()
			
			messages.success(request, 'Appointment created!')
		else:
			messages.error(request, 'Could not create appointment')
		return redirect('provider_appointments')

	def patch(self, request, format=None):
		try:
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
			return Response(serialized_appointment.date, status=status.HTTP_200_OK)
		except:
			return Response('Unable to edit appointment', status=status.HTTP_400_BAD_REQUEST)
