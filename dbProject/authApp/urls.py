from django.urls import path
from .views import logoutuser, patient_registration, loginuser, provider_registration

urlpatterns = [
    path('logout', logoutuser, name="logout"),
    path('patient_registration', patient_registration, name="register_patient"),
    path('provider_registration', provider_registration, name="register_provider"),
    path('login', loginuser, name="login")    
]