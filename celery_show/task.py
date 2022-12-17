from celery import shared_task
from django.contrib.auth import get_user_model
from time import sleep
from django.core.mail import send_mail
import time
@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_task():
    for i in range(10):
        print(i)
    send_mail('CELERY WiTH MAILING','CELERY IS COOL',
        'saikrishnakasa123@gmail.com',
        ['hemanthsaivasa@gmail.com',],
        fail_silently=False
        )
    return "Mail Sent"