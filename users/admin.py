from django.contrib import admin

from users.models import CustomUser, MedicalWorker, Department

admin.site.register(CustomUser)
admin.site.register(MedicalWorker)
admin.site.register(Department)
