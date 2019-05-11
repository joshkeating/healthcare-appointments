from rest_framework import serializers
from .models import Admin


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



class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('username', 'password')