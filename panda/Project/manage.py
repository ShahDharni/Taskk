#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()


















































# Optimized Code
# import pandas as pd
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Student
# from .serializers import StudentSerializers
# import datetime

# CSV_FILE_PATH = 'C:/Users/BAPS/Desktop/Daily Task/panda/StudentsPerformance.csv'

# class StudentListCreateView(APIView):
#     def get(self, request):
#         try:
#             with open(CSV_FILE_PATH, 'r') as file:
#                 df = pd.read_csv(file)
#         except FileNotFoundError:
#             return Response({"error": "CSV file not found"}, status=status.HTTP_404_NOT_FOUND)
#         data = df.to_dict(orient='records')
#         students = Student.objects.all()
#         return Response(data)
    
#     def post(self, request):
#         serializer = StudentSerializers(data=request.data, many=True)
#         if serializer.is_valid():
#             students = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



