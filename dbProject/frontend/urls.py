from django.urls import path
from .views import render_registration, render_homepage, \
    render_login, render_provider_registration, render_patient_prescription, render_provider_prescription

urlpatterns = [
    path('', render_homepage, name="homepage"),
    path('patient_registration', render_registration, name="patient_registration"),
    path('provider_registration', render_provider_registration, name="provider_registration"),
    path('login', render_login, name="loginpage"),
    path('patient_prescription', render_patient_prescription, name="patient_prescription"),
    path('provider_prescription', render_provider_prescription, name="provider_prescription"),

]