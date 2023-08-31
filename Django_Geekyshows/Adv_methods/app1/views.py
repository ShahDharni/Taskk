from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session["name"]="Dharni"
    request.session.set_expiry(5)

    return render(request,'Student/setsession.html')

def getsession(request):
    # name=request.session["name"]
    # or alternative method
    print(request.session.get_expiry_date())
    print(request.session.get_expiry_age())
    print(request.session.get_session_cookie_age())
    print(request.session.get_expire_at_browser_close())

    name=request.session.get("name")
    keys=request.session.keys()
    items=request.session.items()
    # age=request.session.setdefault("age",22)
    return render(request,'Student/getsession.html',{'name':name,"key":keys,"item":items})


def delsession(request):
    request.session.flush()
    # request.clear_expired()
    # if "name" in request.session:
    #     del request.session['name']
    return render(request,'Student/delsession.html')