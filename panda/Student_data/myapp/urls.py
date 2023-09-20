from django.urls import path,include
from.views import StudentListCreateView

urlpatterns = [
    path("student/",StudentListCreateView.as_view())
]
