from django.urls import path
from .views import render_registration, render_homepage, \
    render_login, render_provider_registration

urlpatterns = [
    path('', render_homepage, name="homepage"),
    path('patient_registration', render_registration, name="patient_registration"),
    path('provider_registration', render_provider_registration, name="provider_registration"),
    path('login', render_login, name="loginpage"),
]