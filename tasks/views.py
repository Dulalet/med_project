import datetime
from functools import partial

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, HTTP_201_CREATED

from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.tasks import send_email_notification


class CreateTask(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        created_object = serializer.save(user=self.request.user)
        send_date = created_object.deadline - datetime.timedelta(hours=1)
        send_email_notification.apply_async((self.request.user.email,), eta=send_date, instance=created_object.name)

    def create(self, request, *args, **kwargs):
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            return Response("You don't have a permission to create a task", HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, HTTP_201_CREATED, headers=headers)

class ListTask(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UpdateTask(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if (instance.user.id is not self.request.user.id) and self.request.user.is_superuser is False:
            return Response("You don't have a permission to update this task", HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response('updated', HTTP_202_ACCEPTED)


class DeleteTask(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if (instance.user.id is not self.request.user.id) and self.request.user.is_superuser is False:
            return Response("You don't have a permission to delete this task", HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response('deleted', HTTP_202_ACCEPTED)
