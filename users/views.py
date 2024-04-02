from django.contrib.auth import login , logout
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer , UserRegisterSerializer , UserSerializer
from .validations import custom_validation 
import jwt , datetime
from dotenv import load_dotenv
import os

load_dotenv()

class UserView(APIView):
    def get(self,request):
        return Response(data="Hello",status=201)
    
class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        valid_data =  custom_validation(request.data)
        serializer = UserRegisterSerializer(data=valid_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(valid_data)
            if user:
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	
	def post(self, request):
            data = request.data
            serializer = UserLoginSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                user = serializer.check_user(data)
            payload = {
                'id': user.user_id,
                'exp': datetime.datetime.now() + datetime.timedelta(hours=2),
                'iat': datetime.datetime.now()
            }
            token = jwt.encode(payload,os.getenv('JWT_SECRET_KEY'), algorithm='HS256')
            
            response = Response({"message":"logged in successfully"})
            response.set_cookie(key='jwt',value=token,httponly=True)
            return response


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
	
    def post(self, request):
        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            "message":"logged out successfully"
        }
        return response


class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)

        


