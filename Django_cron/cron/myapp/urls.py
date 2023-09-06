from django.urls import path
from myapp.views import News_Ids,NewsId

urlpatterns = [
    path("newsid/",News_Ids.as_view(),name="Hackernewsid"),
    path("newsid1/",NewsId.as_view(),name="Hackernewsid")

]