from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in,sender=User) # First method
def login_success(sender,user,request,**kwargs):
    print("-----------------")
    print("Logged-In Run Intro")
    print("sender",sender)
    print("user",user)
    print(f'Kwargs:{kwargs}')
    print("request",request)
    print("user password",user.password)

# user_logged_in.connect(login_success,sender=User) another method


@receiver(user_logged_out,sender=User) 
def logout_success(sender,user,request,**kwargs):
    print("-----------------")
    print("Logged-out Run Intro")
    print("sender",sender)
    print("user",user)
    print(f'Kwargs:{kwargs}')
    print("request",request)
    print("user password",user.password)


@receiver(user_login_failed,sender=User) 
def login_failed(sender,credentials,request,**kwargs):
    print("-----------------")
    print("Logged-in-failed")
    print("sender",sender)
    print("credentials",credentials)
    print(f'Kwargs:{kwargs}')
    print("request",request)
