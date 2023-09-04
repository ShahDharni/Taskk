from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method=="GET":
        id=request.data.get(id)
        if id is None:
            stu=Student.objects.get(id=id)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"})
        return Response(serializer.errors)
    
    if request.method=="PUT":
        id=request.data.get(id)
        stu=request.data.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated"})
        return Response(serializer.errors)
     
    if request.method=="DELETE":
        id=request.data.get(id)
        stu=request.data.get(pk=id)
        stu.delete()
        return Response({"Msg":"Data Deleted"})

## By id 
@api_view(['GET','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is None:
            stu=Student.objects.get(pk=id)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    

    if request.method=="PUT":
        id=pk
        stu=request.data.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data Updated"})
        return Response(serializer.errors)
     

    if request.method=="PATCH":
        id=pk
        stu=request.data.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Partial Data Updated"})
        return Response(serializer.errors)
    
    
    if request.method=="DELETE":
        id=pk
        stu=request.data.get(pk=id)
        stu.delete()
        return Response({"Msg":"Data Deleted"})