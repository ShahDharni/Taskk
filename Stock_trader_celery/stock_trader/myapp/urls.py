from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.stockPicker,name='stockpicker'),
    path("stocktracker/",views.stockTracker,name='stocktracker')
    
]
