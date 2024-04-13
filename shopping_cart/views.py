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

        shopping_cart = get_object_or_404(ShoppingCart, user_id=user_id)
        shopping_cart.delete()
        
        return Response({'message': 'Shopping cart deleted successfully'}, status=status.HTTP_200_OK)