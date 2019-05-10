from rest_framework import serializers


class MedicationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    instructions = serializers.CharField()
    recommended_dose = serializers.CharField()