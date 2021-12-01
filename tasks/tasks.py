from celery import shared_task

from django.core.mail import send_mail
from medapp.settings import EMAIL_HOST_USER


@shared_task
def send_email_notification(user):
    send_mail(subject='Notification!',
              message='Deadline for your task is ending in 1 hour!',
              from_email=EMAIL_HOST_USER,
              recipient_list=[user], fail_silently=False)
