from django.shortcuts import render,HttpResponse

# Create your views here.
def setsession(request):
    request.session["name"]="Dharni"
    request.session.set_expiry(5)

    return render(request,'Student/setsession.html')

def getsession(request):
    # name=request.session["name"]
    # or alternative method
   if "name" in request.session:
    name=request.session.get("name")
    return render(request,'Student/getsession.html',{'name':name})
   
   else:
      return HttpResponse("Your Session has expired")


def delsession(request):
    request.session.flush()
    # request.clear_expired()
    # if "name" in request.session:
    #     del request.session['name']
    return render(request,'Student/delsession.html')