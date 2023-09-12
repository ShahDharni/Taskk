from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    email=models.EmailField()
    token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        print("hellooooo-------------")
        self.token=str(uuid.uuid4())
        print(self.token)
        super(Profile,self).save(*args,**kwargs)