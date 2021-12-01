from django.urls import path
from .views import *


urlpatterns = [
    path('tasks/', ListTask.as_view(), name="tasks"),
    path('tasks/create/', CreateTask.as_view(), name="tasks-create"),
    path('tasks/<int:pk>/', UpdateTask.as_view(), name="tasks-update"),
    path('tasks/<int:pk>/delete/', DeleteTask.as_view(), name="tasks-delete"),
]