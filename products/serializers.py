from rest_framework import serializers
from .models import Product, ProductImage

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # exclude = ['product_id']
        fields = '__all__'


    def validate_name(self, value):
        # if Product.objects.filter(name=value).exists():
        #     raise serializers.ValidationError("Product with this name already exists.")
        return value

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, value):
        # if Product.objects.exclude(product_id=self.instance.product_id).filter(name=value).exists():
        #     raise serializers.ValidationError("Product with this name already exists.")
        return value

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
