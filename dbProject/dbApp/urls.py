from django.urls import path
from .views import MedicationAPI, PrescriptionAPI, AdminAPI, AppointmentAPI


urlpatterns = [
    path(r'medications', MedicationAPI.as_view()),
    path(r'prescriptions', PrescriptionAPI.as_view()),
    path(r'appointment', AppointmentAPI.as_view()),
    path(r'admins', AdminAPI.as_view()),
]