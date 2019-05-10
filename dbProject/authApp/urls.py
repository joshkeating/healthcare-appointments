from django.urls import path
from .views import logoutuser, patient_registration

urlpatterns = [
    path('logout', logoutuser, name="logout"),
    path('patient_registration', patient_registration, name="register_patient")
]