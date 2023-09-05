from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'core/index.html')


def about(request):
    return render(request,'core/about.html')


def blog(request):
    return render(request,'core/blog.html')


def contact(request):
    return render(request,'core/contact.html')


def detail(request):
    return render(request,'core/detail.html')


def feature(request):
    return render(request,'core/feature.html')


def product(request):
    return render(request,'core/product.html')


def service(request):
    return render(request,'core/service.html')


def team(request):
    return render(request,'core/team.html')


def testimonial(request):
    return render(request,'core/testimonial.html')