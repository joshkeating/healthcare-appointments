from django.urls import path, include
from .views import MedicationAPI


urlpatterns = [
    path(r'medications', MedicationAPI.as_view())
]