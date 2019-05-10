from rest_framework import serializers


class MedicationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    instructions = serializers.CharField()
    recommended_dose = serializers.CharField()


class PrescriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    patient = serializers.IntegerField()
    medication = serializers.IntegerField()
    date_prescribed = serializers.DateTimeField()
    expiration = serializers.DateField()
    dose = serializers.CharField()