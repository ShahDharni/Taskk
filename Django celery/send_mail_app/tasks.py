from django.contrib.auth import get_user_model
from celery import shared_task

@shared_task(bind=True)
def send_mail_func(self):
    users=get_user_model().objects.all()
    return "done"