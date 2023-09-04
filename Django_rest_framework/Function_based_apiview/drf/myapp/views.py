from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
@api_view(['GET',"POST"])
def hello_world(request):
    if request=="GET":
     return HttpResponse({'msg':"This is GET method"})
    
    # if request=="POST":
    #  print(request.data)
    #  return HttpResponse({'msg':"This is POST method","data":request.data})