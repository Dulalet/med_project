import django.contrib.auth.models
from django.db import models
from rest_framework.authtoken.admin import User


class TaskPriority(models.IntegerChoices):
    LOW = 0, 'Low'
    NORMAL = 1, 'Normal'
    HIGH = 2, 'High'


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    priority = models.IntegerField(default=TaskPriority.LOW, choices=TaskPriority.choices)
    deadline = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE, default=1)

