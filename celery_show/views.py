from django.shortcuts import render
from django.http import HttpResponse
from .task import sleepy,send_mail_task
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json 

def index(request):
    send_mail_task.delay()
    return HttpResponse("<h1>Hello from celery </h1>")

def schedule_mail(request):
    schedule,created=CrontabSchedule.objects.get_or_create(hour=18,minute=43)
    task=PeriodicTask.objects.create(crontab=schedule,name="Schedule mails tahhy 8",task='celery_show.task.send_mail_task')
    return HttpResponse("Schedlued")