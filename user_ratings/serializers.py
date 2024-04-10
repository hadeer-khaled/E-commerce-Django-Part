# serializers.py
from rest_framework import serializers
from .models import user_ratings

class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_ratings
        fields = ['user_id', 'product_id', 'rating']
