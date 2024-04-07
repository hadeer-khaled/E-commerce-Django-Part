from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model , authenticate
from django.contrib.auth.hashers import make_password, check_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'image','email', 'phone', 'user_img']
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'image','email', 'phone']
    
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            role=validated_data['role'],
            username=validated_data['phone']
            )
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, validated_data):
        user = User.objects.get(email=validated_data['email'])
        if not check_password(validated_data['password'],user.password):
            raise ValidationError("Password is not correct")
        if not user:
            raise ValidationError('User not found')
        return user

    def check_admin(self, validated_data):
        user = User.objects.get(email=validated_data['email'])

        if not check_password(validated_data['password'],user.password):
            raise ValidationError("Password is not correct")
        if not user or not user.is_superuser:
            raise ValidationError('Admin not found')
        return user
