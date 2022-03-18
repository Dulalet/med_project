from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models
from medapp.utils import BaseModel, DateModel

# from medapp.settings import PROFILE_PHOTOS_ROOT


class CustomUser(BaseModel, DateModel, AbstractUser):
    categoryChoices = [
        ('patient', 'patient'),
        ('med_worker', 'medical_worker'),
    ]

    genderChoices = [
        ('m', 'male'),
        ('f', 'female'),
    ]

    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=genderChoices, blank=True, null=True)
    category = models.CharField(max_length=32, choices=categoryChoices, default='patient')
    profile_photo = models.ImageField(upload_to='profile_photos')

    def __str__(self):
        return self.first_name + ' ' + self.email


class Department(BaseModel):
    departmentChoices = [
        ('surgery', 'surgery'),
        ('cardiology', 'cardiology'),
        ('pediatrics', 'pediatrics'),
    ]
    name = models.CharField(max_length=32, choices=departmentChoices, blank=False, null=False)
    location = models.CharField(max_length=32, blank=False, null=False)
    # department_head = models.ForeignKey('MedicalWorker', on_delete=models.CASCADE, related_name='department_head')

    def __str__(self):
        return self.name


class MedicalWorker(BaseModel, DateModel):
    categoryChoices = [
        ('doctor', 'doctor'),
        ('nurse', 'nurse'),
    ]
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    is_department_head = models.BooleanField(default=False)
    education = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=32, choices=categoryChoices, default='doctor')
    specialization = models.CharField(max_length=32, blank=True, null=True)
    work_experience = models.CharField(max_length=200, blank=True, null=True)
    years_of_experience = models.SmallIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f'{self.category}: {self.user.first_name} {self.user.email}'
