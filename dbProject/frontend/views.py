from django.shortcuts import render, redirect
from dbApp.forms import PatientRegistrationForm, ProviderRegistrationForm, LoginForm, PrescriptionForm, AppointmentForm, \
    MedicationForm
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from dbApp.models import Prescription, Appointment
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json


def render_registration(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    form = PatientRegistrationForm()
    return render(request, 'patient_registration.html', { "form": form })

def render_provider_registration(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    form = ProviderRegistrationForm()
    return render(request, 'patient_registration.html', { "form": form })

def render_homepage(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return render(request, 'index.html')

def render_login(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    form = LoginForm()
    return render(request, 'login.html', { 'form': form })

def render_patient_prescription(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    try:
        patient = request.user.patient
        return render(request, 'patient_prescription.html')
    except:
        return redirect('homepage')

def render_provider_prescription(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    try:
        provider = request.user.provider
        return render(request, 'provider_prescription.html')
    except:
        return redirect('homepage')

def delete_prescription(request, id):
    try:
        provider = request.user.provider
        get_object_or_404(Prescription, pk=id).delete()
        return redirect('provider_prescription')
    except:
        return redirect('homepage')

def delete_appointment(request, id):
    try:
        provider = request.user.provider
        get_object_or_404(Appointment, pk=id).delete()
        return redirect('provider_appointments')
    except:
        return redirect('homepage')

def render_patient_appointments(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    try:
        patient = request.user.patient
        appointments = Appointment.objects.filter(patient=patient)
        return render(request, 'patient_appointments.html', { 'appointments': appointments })
    except:
        return redirect('homepage')

def render_provider_appointments(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    try:
        provider = request.user.provider
        appointments = Appointment.objects.filter(provider=provider)
        form = AppointmentForm()
        return render(request, 'provider_appointments.html', { 'appointments': appointments, 'form': form })
    except:
        return redirect('homepage')

def render_add_prescription(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    try:
        provider = request.user.provider
    except:
        return redirect('homepage')
    form = PrescriptionForm()
    return render(request, 'add_prescription.html', { 'form': form })


def render_add_medication(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    try:
        provider = request.user.provider
    except:
        return redirect('homepage')
    form = MedicationForm()
    return render(request, 'add_medications.html', { 'form': form })


def chatroompage(request, room_name):
    user = request.user
    if not user.is_authenticated:
        return redirect('homepage')
    try:
        patient = user.patient
        first_name = user.first_name
    except:
        first_name = "Dr."
    finally:
        name = first_name + " " + user.last_name
    return render(request, 'chat/chatroom.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'name': mark_safe(json.dumps(name))
    })

