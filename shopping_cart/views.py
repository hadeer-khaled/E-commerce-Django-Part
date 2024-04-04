from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ShoppingCart
from .serializer import ShoppingCartSerializer
from users import authentication

class DeleteShoppingCartView(APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    def delete(self, request):
        user_id = request.query_params.get('user_id')
        if user_id is None:
            return Response({'error': 'User ID is missing in query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        shopping_cart = get_object_or_404(ShoppingCart, user_id=user_id)
        serializer = ShoppingCartSerializer(shopping_cart)
        shopping_cart.delete()
        return Response({'message': 'Shopping cart deleted successfully', 'deleted_cart': serializer.data}, status=status.HTTP_204_NO_CONTENT)
