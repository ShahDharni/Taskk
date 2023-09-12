from django_celery_project.celery import app
from .models import Profile
import datetime
from django.core.mail import send_mail
from django.conf import settings

@app.task(name="send_notification")
def send_notification():
    try:
        time_threshold= datetime.now() -datetime.timedelta(hours=2)   ## For setting the time
        profile_objs=Profile.objects.filter(created_at_gte=time_threshold)  ## This is all profile objects whose email is not verified within the specified time(i.e 2 hours).

        for profile_obj in profile_objs:
            subject="Notification your account is not verified"
            message="Your account is not verified"
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[profile_obj.email]
            send_mail(subject,message,email_from,recipient_list)

            

    except Exception as e:
        print("e")