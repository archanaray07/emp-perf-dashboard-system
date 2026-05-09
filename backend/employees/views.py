from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Department, EmployeeProfile
from .serializers import DepartmentSerializer, EmployeeProfileSerializer

# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes=[permissions.IsAuthenticated]

class EmployeeProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes=[permissions.IsAuthenticated]
