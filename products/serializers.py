from rest_framework import serializers
from .models import Product, ProductImage

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_payment_id(self, value):
        if Product.objects.filter(payment_id=value).exists():
            raise serializers.ValidationError("Product with this payment_id already exists.")
        return value

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_payment_id(self, value):
        if Product.objects.exclude(pk=self.instance.pk).filter(payment_id=value).exists():
            raise serializers.ValidationError("Product with this payment_id already exists.")
        return value

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
