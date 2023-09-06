from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery import states

os.environ.setdefault('DJANGO_SETTINGS_MODULE','celery.settings')
app=Celery('celery')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings,namespace="CELERY")

## Celery Beat settings

app.autodiscover_tasks
@app.task(bind=True)
def debug_task(self):
    print(f'Requests :{self.request!r}')

