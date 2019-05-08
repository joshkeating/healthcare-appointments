from django.contrib import admin
from .models import AdminUser, Prescription, Medication

admin.site.register(AdminUser),
admin.site.register(Prescription),
admin.site.register(Medication),