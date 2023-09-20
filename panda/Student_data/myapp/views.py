
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student 
from .serializers import StudentSerializer 
import datetime  

class StudentListCreateView(APIView):
    def get(self, request):
        csv_file_path = 'C:/Users/BAPS/Desktop/Daily Task/panda/StudentsPerformance.csv'

        try:
            df = pd.read_csv(csv_file_path)
        except FileNotFoundError:
            return Response({"error": "CSV file not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = df.to_dict(orient='records')
        print("Start", datetime.datetime.now())

        for student_data in data:
            keys = student_data.keys()
            values = student_data.values()
            print(keys)
            print(values)
        
        students = Student.objects.all()
        print("students",students)
        print("End", datetime.datetime.now())

        return Response(data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
















