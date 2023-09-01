from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete,pre_migrate,post_migrate
from django.core.signals import request_finished,request_started,got_request_exception
from django.db.backends.signals import connection_created

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


@receiver(post_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("-----------------")
    print("post_delete")
    print("sender",sender)
    print("instance",instance)
    print(f'Kwargs:{kwargs}')

# post_delete.connect(at_ending_delete,sender=User) another method


@receiver(pre_init,sender=User)
def at_beginning_init(sender,*args,**kwargs):
    print("-----------------")
    print("pre_init")
    print("sender",sender)
    print(f'args:{args}')
    print(f'Kwargs:{kwargs}')

# pre_init.connect(at_beginning_init,sender=User) another method


@receiver(post_init,sender=User)
def at_ending_init(sender,*args,**kwargs):
    print("-----------------")
    print("post_init")
    print("sender",sender)
    print(f'args:{args}')
    print(f'Kwargs:{kwargs}')

# post_init.connect(at_ending_init,sender=User) another method


@receiver(request_started)
def at_request_started(sender,environ,**kwargs):
    print("-----------------")
    print("request started")
    print("sender",sender)
    print("environ",environ)
    print(f'Kwargs:{kwargs}')

# request_started.connect(at_request_started) another method


@receiver(request_finished)
def at_request_ending(sender,**kwargs):
    print("-----------------")
    print("request finished")
    print("sender",sender)
    print(f'Kwargs:{kwargs}')

# request_finished.connect(at_request_ending) another method

    

@receiver(got_request_exception)
def at_exception_request(sender,request,**kwargs):
    print("-----------------")
    print("request exception")
    print("sender",sender)
    print("request",request)
    print(f'Kwargs:{kwargs}')

# got_request_exception.connect(at_exception_request) another method
    

@receiver(pre_migrate)
def at_beginning_migrate(sender,app_config,using,verbosity,interactive,plan,apps,**kwargs):
    print("----------------------------")
    print("Pre Migrate")
    print("sender",sender)
    print("app_config",app_config)
    print("using",using)
    print("verbosity",verbosity)
    print("interactive",interactive)
    print("plan",plan)
    print("apps",apps)
    print(f'Kwargs:{kwargs}')

# pre_migrate.connect(at_beginning_migrate) another method



@receiver(post_migrate)
def at_ending_migrate_flush(sender,app_config,using,verbosity,interactive,plan,apps,**kwargs):
    print("----------------------------")
    print("post migrate")
    print("sender",sender)
    print("app_config",app_config)
    print("using",using)
    print("verbosity",verbosity)
    print("interactive",interactive)
    print("plan",plan)
    print("apps",apps)
    print(f'Kwargs:{kwargs}')

# post_migrate.connect(at_ending_migrate) another method




@receiver(connection_created)
def connect_db(sender,connection,**kwargs):
    print("-----------------")
    print("connection created")
    print("sender",sender)
    print("connection",connection)
    print(f'Kwargs:{kwargs}')


# connection_created.connect(connect_db) another method
