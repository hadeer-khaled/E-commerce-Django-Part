from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ShoppingCart
from .serializer import ShoppingCartSerializer

class DeleteShoppingCartView(APIView):
    def delete(self, request):
        user_id = request.data.get('user_id')
        shopping_cart = get_object_or_404(ShoppingCart, user_id=user_id)
        shopping_cart.delete()

        return Response({'message': 'Shopping cart deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
