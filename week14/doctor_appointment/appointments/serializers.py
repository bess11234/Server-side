from rest_framework import serializers
from .models import *

from django.utils.timezone import now

class DoctorSerializer(serializers.ModelSerializer):
    # appointment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    # appointment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    display_doctor = DoctorSerializer(source="doctor", read_only=True)
    display_patient = PatientSerializer(source="patient", read_only=True)

    class Meta:
        model = Appointment
        fields = ["id", "doctor", "display_doctor", "patient", "display_patient", "date", "at_time", "details", "created_by"]
        extra_kwargs = {
            'doctor': {'write_only': True},
            'patient': {'write_only': True},
        }
    
    def validate(self, valid_data):
        if valid_data['date'] < now().date() or (valid_data['date'] <= now().date() and valid_data['at_time'] < now().time()):
            raise serializers.ValidationError("The appointment date or time must be in the future.")
        return valid_data
