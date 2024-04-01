from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UserView(APIView):
    def get(self,request):
        return Response(data="Hello",status=201)