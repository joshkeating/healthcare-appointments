from django.urls import path, re_path

from .views import render_registration, render_homepage, \
    render_login, render_provider_registration, render_patient_prescription, \
    render_provider_prescription, delete_prescription, render_add_prescription, \
    render_patient_appointments, render_provider_appointments, delete_appointment, \
    render_add_medication, chatroompage 

urlpatterns = [
    path('', render_homepage, name="homepage"),
    path('patient_registration', render_registration, name="patient_registration"),
    path('provider_registration', render_provider_registration, name="provider_registration"),
    path('login', render_login, name="loginpage"),
    path('patient_prescription', render_patient_prescription, name="patient_prescription"),
    path('provider_prescription', render_provider_prescription, name="provider_prescription"),
    path('delete_prescription/<int:id>', delete_prescription, name='delete_prescription'),
    path('delete_appointment/<int:id>', delete_appointment, name='delete_appointment'),
    path('add_prescription', render_add_prescription, name='add_prescription'),
    path('patient_appointments', render_patient_appointments, name='patient_appointments'),
    path('provider_appointments', render_provider_appointments, name='provider_appointments'),
    path('add_medication', render_add_medication, name='add_medication'),
    re_path(r'^chat/(?P<room_name>[^/]+)/$', chatroompage, name='chatroompageN'),

]