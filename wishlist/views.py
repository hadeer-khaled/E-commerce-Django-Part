from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Wishlist
from .serializer import WishlistSerializer
from products.models import Product
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.http import Http404
from users import authentication

class WishlistListView(APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            wishlists = Wishlist.objects.filter(user_id=user_id)
            serializer = WishlistSerializer(wishlists, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'User ID not provided'}, status=status.HTTP_400_BAD_REQUEST)

class AddToWishlistView(APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    def post(self, request):
        product_id = request.data.get('product_id')
        user_id = request.data.get('user_id')

        product = get_object_or_404(Product, pk=product_id)
        wishlist, created = Wishlist.objects.get_or_create(user_id=user_id)
        wishlist.products.add(product)

        wishlist_serializer = WishlistSerializer(wishlist)
        return Response({'message': 'Product added to wishlist successfully', 'added_product': wishlist_serializer.data}, status=status.HTTP_201_CREATED)

class RemoveFromWishlistView(APIView):
    def delete(self, request):
        product_id = request.data.get('product_id')
        user_id = request.data.get('user_id')

        product = get_object_or_404(Product, pk=product_id)
        wishlist = get_object_or_404(Wishlist, user_id=user_id)

        wishlist.products.remove(product)
        deleted_message = 'Product removed from wishlist'

        wishlist_serializer = WishlistSerializer(wishlist)
        return Response({'message': deleted_message, 'removed_product': wishlist_serializer.data}, status=status.HTTP_200_OK)
