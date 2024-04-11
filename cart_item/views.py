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
from django.db.models import Sum

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
    # authentication_classes = (authentication.CustomUserAuthentication,)
    def get(self, request):
        print(request.query_params.get('user_id'))
        user_id = request.query_params.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        shopping_cart = get_object_or_404(ShoppingCart, user=user)
        cart_items = CartItem.objects.filter(cart=shopping_cart)
        
        total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0

        cart_items_count = cart_items.count()

        serializer = CartItemSerializer(cart_items, many=True)
        
        data = {
            'cart_items_count': cart_items_count,
            'total_quantity': total_quantity,
            'cart_items': serializer.data
        }

        return Response(data)


class IncrementCartItemQuantityView(APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    def post(self, request):
        user_id = request.data.get('user_id')
        cart_item_id = request.data.get('cart_item_id')
        user = get_object_or_404(User, pk=user_id)

        shopping_cart = get_object_or_404(ShoppingCart, user=user)
        cart_item = get_object_or_404(CartItem, cart=shopping_cart, cart_item_id=cart_item_id)

        cart_item.quantity += 1
        cart_item.total_price = cart_item.product.price * cart_item.quantity  
        cart_item.save()

        data = CartItemSerializer(cart_item).data
        data['total_price'] = cart_item.total_price

        return Response(data)



class DecrementCartItemQuantityView(APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    def post(self, request):
        user_id = request.data.get('user_id')
        cart_item_id = request.data.get('cart_item_id')
        user = get_object_or_404(User, pk=user_id)

        shopping_cart = get_object_or_404(ShoppingCart, user=user)
        cart_item = get_object_or_404(CartItem, cart=shopping_cart, cart_item_id=cart_item_id)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.total_price = cart_item.product.price * cart_item.quantity
            cart_item.save()

            data = CartItemSerializer(cart_item).data
            data['total_price'] = cart_item.total_price

            return Response(data)
        else:
            cart_item.delete()
            return Response({"detail": "Cart item removed from shopping cart."}, status=status.HTTP_204_NO_CONTENT)


class RemoveFromCartView(APIView):
    def delete(self, request):
        cart_item_id = request.query_params.get('cart_item_id')
        user_id = request.query_params.get('user_id')

        user = get_object_or_404(User, pk=user_id)
        shopping_cart = get_object_or_404(ShoppingCart, user=user)
        cart_item = get_object_or_404(CartItem, cart=shopping_cart, pk=cart_item_id)

        cart_item.delete()

        # Check if the shopping cart is empty after deleting the item
        if shopping_cart.cartitem_set.count() == 0:
            shopping_cart.delete()
            message = 'Shopping cart removed as it is empty.'
        else:
            message = 'Cart item removed from shopping cart.'

        serializer = CartItemSerializer(cart_item)
        return Response({"detail": message, "deleted_cart_item": serializer.data}, status=204)