# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import user_ratings
from .serializers import UserRatingSerializer

class UserRatingView(APIView):
    # def post(self, request):
    #     serializer = UserRatingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = UserRatingSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data.get('user_id')
            product_id = serializer.validated_data.get('product_id')
            rating = serializer.validated_data.get('rating')
            
            # Check if a rating already exists for this user and product
            try:
                existing_rating = user_ratings.objects.get(user_id=user_id, product_id=product_id)
                existing_rating.delete()  # Delete the existing rating
            except user_ratings.DoesNotExist:
                pass  # No existing rating found
            
            # Create a new rating with the provided data
            new_rating = user_ratings.objects.create(user_id=user_id, product_id=product_id, rating=rating)
            return Response(UserRatingSerializer(new_rating).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
            product_id = request.query_params.get('product_id')
            # user_id = request.query_params.get('user_id')

            # if not product_id or not user_id:
            if not product_id:
                return Response({'error': ' product_id '}, status=400)

            try:
                ratings = user_ratings.objects.filter(product_id=product_id)
                # ratings = user_ratings.objects.filter(product_id=product_id, user_id=user_id)
                serialized_ratings = UserRatingSerializer(ratings, many=True)
                return Response(serialized_ratings.data)
            except user_ratings.DoesNotExist:
                return Response({'error': 'No ratings found for the given criteria'}, status=404)
