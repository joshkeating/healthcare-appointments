from django.contrib import admin

from .models import Prescription, Medication, Patient, Provider, Appointment, Admin

# Register your models here.
admin.site.register(Patient)
admin.site.register(Provider)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Medication)
admin.site.register(Admin)
