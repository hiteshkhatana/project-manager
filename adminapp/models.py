from django.db import models

# Create your models here.
class AdminsData(models.Model):
    company = models.CharField(max_length=50)
    admin = models.CharField(max_length=50)

    def __str__(self):
        return self.admin

class EmployeesData(models.Model):
    company = models.CharField(max_length=50)
    admin = models.CharField(max_length=50)
    employee = models.CharField(max_length=50)

    def __str__(self):
        return self.employee

class ProjectsData(models.Model):
    company = models.CharField(max_length=50)
    admin = models.CharField(max_length=50)
    employee = models.CharField(max_length=50)
    project = models.CharField(max_length=500)
    deadline = models.CharField(max_length=20)
    assigned_date = models.DateTimeField()

    def __str__(self):
        return self.project
