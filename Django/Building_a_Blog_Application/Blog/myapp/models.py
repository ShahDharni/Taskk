
# A model is a Python class that subclasses django.db.models.Model, in which each attribute represents a database field. When you create a model, Django offers you a practical API to query the 
# database easily.

from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    status_choices=("draft","Draft"),
    ("published","Published")

    title=models.CharField(max_length=80)
    slug=models.SlugField(max_length=60,unique_for_date="publish")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    published_at=models.DateTimeField(default=timezone.now)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=60,default="draft",choices=status_choices)


    ## Canonical Urls for models
    def get_absolute_query(self):
         return reverse('blog : post_details',args=[self.publish.year,
                                                    self.publish.strftime('%d'),
                                                    self.publish.strftime('%m'),
                                                    self.slug])
    


class Meta:
    ordering="publish"

def __str__(self):
    self.title


## Custom Model Manager
class Published_Manager(models.Manager):
    def get_queryset(self):
            return super(Published_Manager,
                         self).get_queryset()\
                         .filter(status="published")
    
    
#      objects=models.Manager() #--default manager
#      published=Published_Manager() #-- Our custom manager



