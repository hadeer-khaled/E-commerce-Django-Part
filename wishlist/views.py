from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Wishlist
from .serializer import WishlistSerializer
from products.models import Product 
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.http import Http404
from utils.query_params import handle_query_params
from users import authentication
from rest_framework import permissions

class WishlistListView(APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        wishlists = Wishlist.objects.all()
        params = request.query_params
        search_fields = ['wishlist_id'] 

        try:
            result = handle_query_params(wishlists, params, search_fields)
            serializer = WishlistSerializer(result['data'], many=True)
            response_data = {
                'wishlists': serializer.data,
                'current_page': result['current_page'],
                'total_pages': result['total_pages'],
                'total_count': result['total_count']
            }
            return Response(response_data)
        except ValidationError as e:
            return Response({'error': str(e)}, status=400)

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WishlistDetailView(APIView):
    def get_object(self, pk):
        try:
            return Wishlist.objects.get(pk=pk)
        except Wishlist.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        wishlist = self.get_object(pk)
        serializer = WishlistSerializer(wishlist)
        return Response(serializer.data)

    def put(self, request, pk):
        wishlist = self.get_object(pk)
        serializer = WishlistSerializer(wishlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        wishlist = self.get_object(pk)
        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddToWishlistView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        user_id = request.data.get('user_id')  # Assuming you have a user_id associated with the wishlist
        
        product = get_object_or_404(Product, pk=product_id)
        # Check if a wishlist already exists for the user
        wishlist, created = Wishlist.objects.get_or_create(user_id=user_id)
        
        # If the wishlist already exists and the product is not already in the wishlist,
        # add the product to the wishlist
        if not created and not wishlist.products.filter(pk=product_id).exists():
            wishlist.products.add(product)
            return Response({'message': 'Product added to wishlist successfully'}, status=status.HTTP_201_CREATED)
        # If the wishlist already exists and the product is already in the wishlist,
        # return a message indicating that the product is already in the wishlist
        elif not created and wishlist.products.filter(pk=product_id).exists():
            return Response({'message': 'Product already exists in the wishlist'}, status=status.HTTP_200_OK)
        # If a new wishlist was created, add the product to the wishlist
        elif created:
            wishlist.products.add(product)
            return Response({'message': 'Product added to new wishlist successfully'}, status=status.HTTP_201_CREATED)

class RemoveFromWishlistView(APIView):
    def delete(self, request, wishlist_item_id):
        wishlist_item = get_object_or_404(Wishlist, pk=wishlist_item_id)
        wishlist_item.delete()
        
        return Response({'message': 'Product removed from wishlist successfully'}, status=status.HTTP_204_NO_CONTENT)


