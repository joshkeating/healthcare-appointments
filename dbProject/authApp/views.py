from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from dbApp.forms import PatientRegistrationForm


def logoutuser(request):
	logout(request)
	#Show message
	messages.success(request,('You have been logged out.'))
	# Redirect to a success page.
	return redirect('homepage')


def patient_registration(request):
	if request.method != "POST":
		return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
	form = PatientRegistrationForm(request.POST)
	# register user
	messages.success(request,('You have been registered.'))
	return redirect('homepage')
