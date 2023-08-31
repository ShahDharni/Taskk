from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User

def login_success(sender,user,request,**kwargs):
    print("-----------------")
    print("Logged-In Run Intro")
    print("sender",sender)
    print("user",user)
    print(f'Kwargs:{kwargs}')
    print("request",request)
    print("user password",user.password)

user_logged_in.connect(login_success,sender=User)