from django.urls import path
from .views import MedicationAPI, PrescriptionAPI, AdminAPI, AppointmentAPI


urlpatterns = [
    path(r'medications', MedicationAPI.as_view()),
    path(r'prescriptions', PrescriptionAPI.as_view(), name="prescriptions"),
    path(r'appointments', AppointmentAPI.as_view(), name="appointments"),
    path(r'admins', AdminAPI.as_view()),
]