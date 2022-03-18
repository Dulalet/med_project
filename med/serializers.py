from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from rest_framework import serializers

from django.contrib.auth.models import BaseUserManager

from med.models import Appointment
from users.models import MedicalWorker

User = get_user_model()


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        exclude = ['uuid', 'created_at', 'updated_at']
