from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True)
def send_mail_func(self):
    users=get_user_model().objects.all()

    for user in users:
        mail_subject="Hi! celery Testing"
        message = "Hello"
        to_mail=user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_mail],
            fail_silently=True      ## If mail fails while sending to someone it will fail silently without affecting others.

              )
    return "done"