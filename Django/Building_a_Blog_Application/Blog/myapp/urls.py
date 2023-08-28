from django.contrib import admin
from django.urls import path,re_path
from .models import Post
from .views import post_detail,post_list
from .import views


urlpatterns=[
    path("postdetails/",views.post_detail),
    path("postlist/",views.post_list)

]