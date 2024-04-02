from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'user_id', 'order_date', 'total_amount', 'total_quantity','shipment_id', 'address','city' ,'payment_id' ]

