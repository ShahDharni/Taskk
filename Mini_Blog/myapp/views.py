from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "blog/index.html")


def blog(request):
    return render(request, "blog/blog.html")


def contact(request):
    return render(request, "blog/contact.html")


def category(request):
    return render(request, "blog/category.html")


def single(request):
    return render(request, "blog/single.html")
