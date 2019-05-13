from django.contrib import admin

from .models import Prescription, Medication, Patient, Provider, Appointment, Admin

admin.site.register(Patient)
admin.site.register(Provider)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Medication)
admin.site.register(Admin)


# @admin.register(Prescription, Medication, Appointment)
# class GeneralAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Patient, Provider)
# class UserAdmin(admin.ModelAdmin):
#     pass