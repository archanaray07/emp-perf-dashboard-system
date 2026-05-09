from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'role',
        ]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'phone',
            'role',
        ]
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            first_name=validated_data.get('first_name',''),
            last_name=validated_data.get('last_name',''),
            email=validated_data.get('email',''),
            password=validated_data['password'],
            role=validated_data.get('role',''),
            phone=validated_data.get('phone','')
        )
        return user