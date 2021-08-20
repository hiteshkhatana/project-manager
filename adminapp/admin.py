from django.contrib import admin
from .models import AdminsData, EmployeesData, ProjectsData

# Register your models here.
admin.site.register(AdminsData)

admin.site.register(EmployeesData)

admin.site.register(ProjectsData)