from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, message, to):
    recipient_list = [to]

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=True,
    )
