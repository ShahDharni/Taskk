from django.db import models
from datetime import datetime

# Create your models here.
class HackernewsId(models.Model):
    hackernews=models.BigIntegerField(unique=True,primary_key=True)
    fetched_at=models.DateField(default=datetime.now())


    def save(self,*args,**kwargs):
        self.id=self.hackernews # replacing the id(primary key) as the hackernews id
        super(HackernewsId,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.hackernews)
    


## Explanation :-

# In this API, what is needed from the external endpoint is the ids of the external news data. 
# Therefore, you will make the model with just two properties, the id and the datetime fetched.
# The best is to let the fetched ids be the primary keys of the database.
# They are needed to get the latest news from the external endpoint.


# Note: The save method under the class HackerNewsID saves data when called. This only formats the primary key to the id fetched.
