
# import pandas as pd
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student 
# from .serializers import StudentSerializers 
# import datetime  

# class StudentListCreateView(APIView):
#     def get(self, request):
#         csv_file_path = 'C:/Users/BAPS/Desktop/Daily Task/panda/StudentsPerformance.csv'

#         try:
#             df = pd.read_csv(csv_file_path)
#         except FileNotFoundError:
#             return Response({"error": "CSV file not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         data = df.to_dict(orient='records')
#         print("Start", datetime.datetime.now())

#         for student_data in data:
#             keys = student_data.keys()
#             values = student_data.values()
#             print(keys)
#             print(values)
        
#         students = Student.objects.all()
#         print("students",students)
#         print("End", datetime.datetime.now())

#         return Response(data)
    
#     def post(self, request):
#         serializer = StudentSerializers(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()  
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


# Optimized Code
import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializers
import datetime

CSV_FILE_PATH = 'C:/Users/BAPS/Desktop/Daily Task/panda/StudentsPerformance.csv'

class StudentListCreateView(APIView):
    def get(self, request):
        try:
            with open(CSV_FILE_PATH, 'r') as file:
                df = pd.read_csv(file)
        except FileNotFoundError:
            return Response({"error": "CSV file not found"}, status=status.HTTP_404_NOT_FOUND)
        data = df.to_dict(orient='records')
        students = Student.objects.all()
        return Response(data)
    
    def post(self, request):
        serializer = StudentSerializers(data=request.data, many=True)
        if serializer.is_valid():
            students = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



