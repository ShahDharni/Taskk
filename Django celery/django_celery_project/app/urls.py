from django.urls import path,include
from app import views 

urlpatterns = [
    path("test/",views.test),
    path("sendmail/",views.send_mail_to,name="sendmail")
]
