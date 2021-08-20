from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout , get_user_model
from django.core.mail import send_mail


from .models import AdminsData , EmployeesData , ProjectsData

# Create your views here.
def main(request):

    if request.user.is_authenticated:
        if request.user.is_superuser:
            logout(request)
        
        elif request.user.is_staff:
            return redirect('/admin-dashboard')
        
        else:
            return redirect(f"/employee-dashboard")
    
    if request.method == "POST":

        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin-dashboard')
            else:
                return redirect(f"/employee-dashboard")


    return render(request , 'main.html')

def create_admin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password =request.POST.get('password')
        company = request.POST.get('company')

        admin_list = AdminsData.objects.values_list('admin' , flat=True)

        if username in admin_list:
            return render(request , 'create-admin.html')


        user = User.objects.create_user(username, email ,password)  
        user.is_staff=True 
        user.save()

        AdminsData.objects.create(company = company , admin = username)

        login(request, user)

        return redirect('/admin-dashboard')

    return render(request , 'create-admin.html')

def admin_dashboard(request):

    obj = AdminsData.objects.get(admin = request.user.username)

    context = {
        "company" : obj.company,
        "admin" : obj.admin
    }
    return render(request , 'adminapp/admin.html' , context)




def invite(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email_address = request.POST.get('email')
        password =request.POST.get('password')
        message = request.POST.get('message')

        message = message + f"\n\n\n Here are your login credentials - \n Username - {username} \n Password - {password}"
        
        send_mail(subject='Invitation to join' , message=message , from_email= request.user.email , recipient_list=[email_address] , fail_silently=False)
        
        user = User.objects.create_user(username, email_address ,password)  
        
        user.save()

        obj = AdminsData.objects.get(admin = request.user.username)

        EmployeesData.objects.create(company = obj.company , admin = request.user.username , employee = username)

    return render(request, 'adminapp/invite.html')

def project(request):
    employees_list = EmployeesData.objects.values_list('employee' , flat=True)
    obj = AdminsData.objects.get(admin = request.user.username)

    context = {
        'employees' : list(employees_list)
    }

    if request.method == "POST":
        project = request.POST.get('project')
        employee = request.POST.get('employee')
        deadline = request.POST.get('deadline')

        ProjectsData.objects.create(company = obj.company , admin = obj.admin , employee = employee , project = project, deadline = deadline)
        

    return render(request, 'adminapp/project.html' , context)

def logout_view(request):

    logout(request)

    return redirect('/')