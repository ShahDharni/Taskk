from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = (
    [path("", views.home), 
     path("blog", views.blog,name="blog"),
     path("home",views.home,name="home"),
     path("contact",views.contact,name="contact"),
     path("category",views.contact,name="category"),
     path("single",views.contact,name="single"),

     
     ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
