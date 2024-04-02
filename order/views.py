from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer

class AllOrdersView(APIView):
    def get(self,request ):
    
        orders = Order.objects.all()
        if orders.exists():  # Check if there are any orders
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No orders found"}, status=status.HTTP_404_NOT_FOUND)
        
class SpecificOrderView(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(order_id=order_id)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"error": "Order does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
class SpecificUserOrdersView(APIView):
    def get(self, request, user_id):
        try:
            orders = Order.objects.filter(user_id=user_id)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        


