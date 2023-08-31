from django.shortcuts import render

# Create your views here.
def home(request):
    ct=request.session.get("count",0)
    new_ct=ct+1
    request.session['count']=new_ct
    return render(request,'Counter/home.html',{'c':new_ct})