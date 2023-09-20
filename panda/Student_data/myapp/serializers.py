from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('gender','race_ethnicity','Parental_level_of_education','lunch','test_preparation','math_score','reading_score','writing_score')
