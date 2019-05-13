from django.shortcuts import render
from dbApp.forms import PatientRegistrationForm, ProviderRegistrationForm
from rest_framework import status
from rest_framework.response import Response


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

def render_patient_login(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return render(request, 'patient_login.html')

def render_provider_login(request):
    if request.method != "GET":
        return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return render(request, 'provider_login.html')
