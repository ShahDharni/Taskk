from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from.serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.
class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is None:
            stu=Student.objects.get(id=id)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    

    def post(self,request,format=None):
        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"})
        

    def put(self,request,format=None,pk=None):
        if request.method=="PUT":
           id=pk
           stu=Student.objects.get(stu,data=request.data,id=id)
           serializer= StudentSerializer(data=request.data)
           if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated"})
                    






