from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer (serializers.ModelSerializer):
    class Meta:
        model=Wishlist
        fields='__all__'
        # fields:['wishlist_id','user',' products']