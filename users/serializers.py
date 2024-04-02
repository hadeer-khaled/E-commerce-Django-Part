from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model , authenticate

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'username', 'image','email', 'phone']

