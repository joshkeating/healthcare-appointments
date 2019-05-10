from django.urls import path
from .views import MedicationAPI


urlpatterns = [
    path(r'medications', MedicationAPI.as_view()),
]