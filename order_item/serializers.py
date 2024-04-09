from rest_framework import serializers
from .models import Order_Item, Product

# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order_Item
#         fields = ['order_item_id', 'product_id', 'order_id', 'quantity', 'product_price']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         # Fetch related product data
#         product_id = representation['product_id']
#         try:
#             product = Product.objects.get(pk=product_id)
#             representation['product'] = {
#                 'name': product.name,
#                 'price': product.price,
#                 'avg_rating': product.avg_rating,
#                 'image': product.image,
#             }
#         except Product.DoesNotExist:
#             representation['product'] = None
#         return representation

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = ['order_item_id', 'product_id', 'order_id', 'quantity', 'product_price']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Fetch related product data
        product_id = representation['product_id']
        try:
            product = Product.objects.get(pk=product_id)
            representation['product'] = {
                'name': product.name,
                'price': product.price,
                'avg_rating': product.avg_rating,
                'image': self.get_image_url(product.image),
            }
        except Product.DoesNotExist:
            representation['product'] = None
        return representation

    def get_image_url(self, image_field):
        if image_field and hasattr(image_field, 'url'):
            return self.context['request'].build_absolute_uri(image_field.url)
        return None