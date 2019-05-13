from django.urls import path
from .views import MedicationAPI, PrescriptionAPI, AdminAPI


urlpatterns = [
    path(r'medications', MedicationAPI.as_view()),
    path(r'prescriptions', PrescriptionAPI.as_view()),
    path(r'admins', AdminAPI.as_view()),
]