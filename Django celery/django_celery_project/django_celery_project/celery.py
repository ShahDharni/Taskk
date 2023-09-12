from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery import states
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery_project.settings')
app=Celery('celery')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings,namespace="CELERY")

## Celery Beat settings

app.autodiscover_tasks(lambda:settings.INSTALLED_APPS) ## It will auto discover all the task which are mentioned in the list
app.conf.beat_schedule= {
   ' add-every-2-hour':{
       'task':'send_notification',
       'schedule':crontab(minute='*/1')
   }
    }



@app.task(bind=True)
def debug_task(self):
    print(f'Requests :{self.request!r}')


@app.task
def print_hello():
    print("Hello from function")



# unbc fkag gybb stnp ---password