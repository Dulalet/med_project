from django.db import models

from medapp import settings
from medapp.utils import BaseModel, DateModel
from users.models import MedicalWorker

CustomUser = settings.AUTH_USER_MODEL


class Prescription(BaseModel, DateModel):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(MedicalWorker, on_delete=models.CASCADE)
    due_date = models.DateField(blank=True, null=True)
    medicine = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=True, null=True)


class Appointment(BaseModel, DateModel):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(MedicalWorker, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField(blank=False, null=False)
    location = models.CharField(max_length=128, blank=True, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'patient: {self.patient.first_name} {self.patient.last_name}, ' \
               f'doctor: {self.doctor.user.first_name} {self.doctor.user.first_name}'

class MedicalStatus(BaseModel):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=32, blank=False, null=False)
    allergies = models.TextField(blank=True, null=True)
    disease_history = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

