from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(required=False)
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['product_id', 'name', 'price', 'price','stock', 'description','description','category_id','image']


