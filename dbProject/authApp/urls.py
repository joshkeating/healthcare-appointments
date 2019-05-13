from django.urls import path
from .views import logoutuser, patient_registration, loginuser

urlpatterns = [
    path('logout', logoutuser, name="logout"),
    path('patient_registration', patient_registration, name="register_patient"),
    path('provider_registration', patient_registration, name="register_provider"),
    path('login', loginuser, name="login")    
]