from django.urls import path, include

# from users.views import MedWorkerViewSet
from .views import *
from rest_framework.routers import SimpleRouter


# router = SimpleRouter()
# router.register(r'med_worker', MedWorkerViewSet)

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('departments/<str:department_name>/', doctors_by_department),
    path('appointments/', appointments),
    # path('', include(router.urls)),
]