from rest_framework import serializers
from .models import Department, EmployeeProfile

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeProfileSerializer(serializers.ModelSerializer):
    user_details = serializers.StringRelatedField(source='users', read_only=True)
    manager_details = serializers.StringRelatedField(source='manager', read_only=True)

    class Meta:
        model = EmployeeProfile
        fields = [ 'id', 
                'user',
                'user_details', 
                'employee_id', 
                'department', 
                'designation', 
                'joining_date', 
                'manager', 
                'manager_details', 
                'skills',
            ]