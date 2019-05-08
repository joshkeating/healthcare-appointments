from django.contrib import admin

from .models import Admin, Prescription, Medication, Patient, Provider, Appointment

# Register your models here.
admin.site.register(Patient)
admin.site.register(Provider)
admin.site.register(Appointment)
admin.site.register(Admin)
admin.site.register(Prescription)
admin.site.register(Medication)
