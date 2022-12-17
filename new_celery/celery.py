import os
from celery import Celery
from . import settings
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_celery.settings')

from celery.schedules import crontab
# from django_celery_beat.models import PeriodicTask
app = Celery('new_celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django apps.
# celery Beat settings
app.conf.beat_schedule={
    'send_mail_everyday_at_8':{
        'task':'celery_show.task.send_mail_task',
        'schedule':crontab(hour=3,minute=59),
        # 'args':(2,23,3)..these args can be used in the function if needed
        # To schedule a job crontab is used
        # we can use to send args to the function 'args':(2)
    }
}
app.autodiscover_tasks()

#To start celery beat use : celery -A <project_name> beat -l info

app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


#To start Celery worker 
#celery -A new_celery  worker --pool=solo  -l  info