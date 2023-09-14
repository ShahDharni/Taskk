from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
# from celery.schedules import crontab  ----> For scheduling the task we use cron tab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','stock_trader.settings')
app=Celery('stock_trader')

app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')
app.conf.beat_schedule={
    'every-10-seconds':{
        'task':'myapp.tasks.update_stock',
        'schedule':10,
        'args':(['RELIANCE.NS','BAJAJ-AUTO.NS'],)

    },
}

app.autodiscover_tasks()
@app.task(bind=True)
def debug(self):
    print(f'Request:{self.request!r}')