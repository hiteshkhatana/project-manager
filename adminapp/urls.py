from django.urls import path
from . import views

urlpatterns = [
    path('' , views.main , name = 'main'),
    path('createadmin/' , views.create_admin , name = 'createadmin'),
    path('logout/' , views.logout_view , name = 'logout'),
    path('admin-dashboard/' , views.admin_dashboard , name = 'admindashboard'),
    path('invite/' , views.invite , name = 'invite'),
    path('project/' , views.project , name = 'project'),

]
