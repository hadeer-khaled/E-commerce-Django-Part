from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserView(APIView):
    def get(self,request):
        return Response(data="Hello",status=201)

class OneUserView(APIView):
    def get(self,request, user_id ):
        try:
            user = User.objects.get(user_id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

