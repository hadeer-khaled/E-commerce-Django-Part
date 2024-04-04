from rest_framework import serializers
from .models import Wishlist
from products.serializers import ProductSerializer  

class WishlistSerializer (serializers.ModelSerializer):
    products = ProductSerializer(many=True) 
    class Meta:
        model=Wishlist
        fields = ['wishlist_id', 'user', 'category_id', 'products']  
        fields='__all__'
        # fields:['wishlist_id','user',' products']
