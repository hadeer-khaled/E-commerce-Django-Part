# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import user_ratings
from .serializers import UserRatingSerializer

class UserRatingView(APIView):
    def post(self, request):
        serializer = UserRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
