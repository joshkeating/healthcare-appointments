from django.contrib import admin
from .models import Patient, Provider, Appointment

# Register your models here.
admin.site.register(Patient)
admin.site.register(Provider)
admin.site.register(Appointment)

