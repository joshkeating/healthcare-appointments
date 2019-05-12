from rest_framework import serializers
from .models import Admin, Prescription


class MedicationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    instructions = serializers.CharField()
    recommended_dose = serializers.CharField()


class PrescriptionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    patient = serializers.RelatedField(source='Patient.id', read_only=True)
    medication = serializers.RelatedField(source='Medication.id', read_only=True)

    class Meta:
        model = Prescription
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')


class AppointmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date_time = serializers.DateTimeField()
    duration = serializers.TimeField()
    patient = serializers.IntegerField()
    provider = serializers.IntegerField()
    note = serializers.CharField()
