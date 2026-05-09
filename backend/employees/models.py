from django.db import models
from django.conf import settings

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)

class EmployeeProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee_profile')
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_employees')
    skills = models.TextField(blank=True)