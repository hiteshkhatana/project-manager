from django.urls import path
from . import views

urlpatterns = [

    path('' , views.employee_dashboard , name = 'employeedashboard'),
    path('projects/<str:pk>' , views.project_detail , name = "projectdetail")

]