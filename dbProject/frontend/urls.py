from django.urls import path
from .views import render_registration, render_homepage, \
    render_patient_login, render_provider_login, render_provider_registration

urlpatterns = [
    path('', render_homepage, name="homepage"),
    path('patient_registration', render_registration, name="patient_registration"),
    path('provider_registration', render_provider_registration, name="provider_registration"),
    path('patient_login', render_patient_login, name="patient_login"),
    path('provider_login', render_provider_login, name="provider_login")
]