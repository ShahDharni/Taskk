from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete

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
    
# user_logged_out.connect(logout_success,sender=User) another method


@receiver(user_login_failed) 
def login_failed(sender,credentials,request,**kwargs):
    print("-----------------")
    print("Log-in-failed")
    print("sender",sender)
    print("credentials",credentials)
    print(f'Kwargs:{kwargs}')
    print("request",request)

# user_login_failed.connect(login_failed,sender=User) another method


@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("-----------------")
    print("Pre save")
    print("sender",sender)
    print("instance",instance)
    print(f'Kwargs:{kwargs}')

# pre_save.connect(at_beginning_save,sender=User) another method


@receiver(post_save,sender=User)
def at_end_save(sender,instance,created,**kwargs):
    if created:
        print("-----------------")
        print("post save")
        print("New Record")        ## If created is True then new record will be craeted
        print("sender",sender)
        print("instance",instance)
        print("created",created)
        print(f'Kwargs:{kwargs}')
    else:
        print("-----------------")
        print("post save")
        print("Update")            ## If not then it will be updated.
        print("sender",sender)
        print("instance",instance)
        print("created",created)
        print(f'Kwargs:{kwargs}')


# post_save.connect(at_end_save,sender=User) another method



@receiver(pre_delete,sender=User)
def at_beginning_delete(sender,instance,**kwargs):
    print("-----------------")
    print("pre_delete")
    print("sender",sender)
    print("instance",instance)
    print(f'Kwargs:{kwargs}')

# pre_delete.connect(at_beginning_delete,sender=User) another method
