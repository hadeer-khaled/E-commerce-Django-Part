from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Order_Item
from .serializers import OrderItemSerializer

from products.models import Product

class OrderItemDetailView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, order_id):
        order_items = Order_Item.objects.filter(order_id=order_id)
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)