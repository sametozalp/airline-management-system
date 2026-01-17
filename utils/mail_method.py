from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, message, to):
    try:      
        recipient_list = [to]

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=True,
        )

    except Exception as e:
        print(e)
