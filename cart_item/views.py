from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CartItem
from .serializer import CartItemSerializer
from users.models import User
from shopping_cart.models import ShoppingCart
from products.models import Product
from users import authentication

class AddToCartView(APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    def post(self, request):
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')
        user = get_object_or_404(User, pk=user_id)
        product = get_object_or_404(Product, pk=product_id)

        shopping_cart, _ = ShoppingCart.objects.get_or_create(user=user)

        cart_item, created = CartItem.objects.get_or_create(cart=shopping_cart, product=product)
        if created:
            cart_item.quantity = 1  
        else:
            cart_item.quantity = cart_item.quantity or 0
            cart_item.quantity += 1
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ViewCartItems(APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,
    def get(self, request):
        user_id = request.query_params.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        shopping_cart = get_object_or_404(ShoppingCart, user=user)
        cart_items = CartItem.objects.filter(cart=shopping_cart)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
