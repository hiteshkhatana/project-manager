from django.shortcuts import render , get_list_or_404 , get_object_or_404
from adminapp.models import EmployeesData , ProjectsData

# Create your views here.
def employee_dashboard(request):
    obj = EmployeesData.objects.get(employee = request.user.username)
    
    projects_obj  = ProjectsData.objects.filter(employee = request.user.username)

    context = {
        "company" : obj.company,
        "admin" : obj.admin,
        'projects' : list(projects_obj)
    }

    
    return render(request , 'employees/employee.html' , context)


def project_detail(request , pk):

    obj = get_object_or_404(ProjectsData , id = pk)

    context = {
        'project_obj' : obj
    }

    print(obj)

    return render(request , 'employees/projectdetail.html' , context)