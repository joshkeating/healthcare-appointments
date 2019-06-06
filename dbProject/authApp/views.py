from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from dbApp.forms import PatientRegistrationForm, ProviderRegistrationForm, LoginForm
from dbApp.models import Patient, Provider


def loginuser(request):
	form = LoginForm(request.POST)
	if form.is_valid():
		user = authenticate(
			request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
		if user is not None:
			login(request, user)
			messages.success(request, ('You have successfully logged in...'))
			return redirect('homepage')
		else:
			messages.error(request, 'Incorrect credentials.')
			return redirect('loginpage')
	else:
		return redirect('loginpage')


def logoutuser(request):
	logout(request)
	# Show message
	messages.success(request, ('You have been logged out.'))
	# Redirect to a success page.
	return redirect('homepage')


def patient_registration(request):
	if request.method != "POST":
		return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
	form = PatientRegistrationForm(request.POST)
	if form.is_valid():
		if form.cleaned_data['password1'] == form.cleaned_data['password2']:
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			user = User.objects.create_user(username, email, password, first_name=first_name,
											last_name=last_name)
			birthdate = form.cleaned_data['birthdate']
			age = form.cleaned_data['age']
			provider = form.cleaned_data['provider']
			allergies = form.cleaned_data['allergies']
			patient = Patient(user=user, birthdate=birthdate, age=age, provider=provider,
							  allergies=allergies)
			# add to provider list of patients
			patient.save()
			provider.patients.add(patient)
			provider.save()
			messages.success(request, ('You have been registered.'))
			login(request, user)
			return redirect('homepage')
		else:
			messages.error(request, 'Passwords do not match.')
			return redirect('patient_registration')
	else:
		messages.error(request, 'Invalid registration request.')
		return redirect('patient_registration')


def provider_registration(request):
	if request.method != "POST":
		return Response('Method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
	form = ProviderRegistrationForm(request.POST)
	if form.is_valid():
		if form.cleaned_data['password1'] == form.cleaned_data['password2']:
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			user = User.objects.create_user(username, email, password, first_name=first_name,
											last_name=last_name)
			phone_number = form.cleaned_data['phone_number']
			patients = form.cleaned_data['patients']
			provider = Provider(
				user=user, phone_number=phone_number)
			if len(patients) > 0:
				provider.patients.set(patients)
			provider.save()
			messages.success(request, ('You have been registered.'))
			return redirect('homepage')
		else:
			messages.error(request, 'Passwords do not match.')
			return redirect('provider_registration')
	else:
		messages.error(request, 'Invalid registration request.')
		return redirect('provider_registration')
