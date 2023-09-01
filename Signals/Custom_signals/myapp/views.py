from django.shortcuts import render,HttpResponse
from myapp import signals

# Create your views here.
def home(request):
    signals.notification.send(sender=None, request=request,user=['Dharni','admin'])
    return HttpResponse("This is Home Page")