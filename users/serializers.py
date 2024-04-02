from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model , authenticate

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'username', 'image','email', 'phone', 'user_img']
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            role=validated_data['role'],
            # user_img=validated_data['user_img']
            )
            
        user.username = validated_data['username']
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()
	
	def check_user(self, validated_data):
		user = authenticate(username=validated_data['email'], password=validated_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['email', 'username']