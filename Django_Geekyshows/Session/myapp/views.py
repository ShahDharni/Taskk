from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session["name"]="Dharni"
    request.session["lname"]="Shah"

    return render(request,'Student/setsession.html')

def getsession(request):
    # name=request.session["name"]
    # or alternative method
    name=request.session.get("name")
    lname=request.session.get("lname")

    return render(request,'Student/getsession.html',{'name':name,"lname":lname})


def delsession(request):
    if "name" in request.session:
        del request.session['name']
    return render(request,'Student/delsession.html')