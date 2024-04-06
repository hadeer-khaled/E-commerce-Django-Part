from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from shipment.models import Shipment
from shipment.models import Shipment
from .serializers import OrderSerializer

class AllOrdersView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request ):
        orders = Order.objects.all()
        if orders.exists():  # Check if there are any orders
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No orders found"}, status=status.HTTP_404_NOT_FOUND)
        
class SpecificOrderView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, order_id):
        try:
            order = Order.objects.get(order_id=order_id)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"error": "Order does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, order_id):
        try:
            order = Order.objects.get(order_id=order_id)
            shipment = order.shipment_id
            # new_status = request.query_params.get('shipmentStatus')
            shipment.status = "cancelled"
            shipment.save()
            return Response("Shipment status updated successfully.", status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return  Response({"error": "Order does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except shipment.DoesNotExist:
            return Response({"error": "Shipment does not exist for this order."}, status=status.HTTP_404_NOT_FOUND)

        
class SpecificUserOrdersView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, user_id):
        try:
            orders = Order.objects.filter(user_id=user_id)       
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        


