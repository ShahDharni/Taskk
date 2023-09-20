from django.db import models

# Create your models here.

class Student(models.Model):
    gender = models.CharField(max_length=10)
    race_ethnicity = models.CharField(max_length=50)
    Parental_level_of_education = models.CharField(max_length=100)
    lunch = models.CharField(max_length=50)
    test_preparation = models.CharField(max_length=50)
    math_score = models.IntegerField()
    reading_score = models.IntegerField()
    writing_score = models.IntegerField()
    
    def __str__(self):
        return self.gender  
