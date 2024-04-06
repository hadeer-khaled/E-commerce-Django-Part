from rest_framework import serializers
from .models import Order
from shipment.models import Shipment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'user_id', 'order_date', 'total_amount', 'total_quantity','shipment_id', 'address','city' ,'payment_id' ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Fetch related shipment data
        shipment_id = representation['shipment_id']
        try:
            shipment = Shipment.objects.get(pk=shipment_id)
            representation['shipment'] = {
                'status': shipment.status,
            }
        except Shipment.DoesNotExist:
            representation['shipment'] = None
        return representation
