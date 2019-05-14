from django.shortcuts import render
from dbApp.forms import PatientRegistrationForm, ProviderRegistrationForm, LoginForm
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from dbApp.models import Prescription


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
    return render(request, 'index.html', {})

def render_login(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    form = LoginForm()
    return render(request, 'login.html', { 'form': form })

def render_patient_prescription(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return render(request, 'patient_prescription.html')

def render_provider_prescription(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return render(request, 'provider_prescription.html')


def delete_prescription(request, id):
    get_object_or_404(Prescription, pk=id).delete()
    return render(request, 'provider_prescription.html')