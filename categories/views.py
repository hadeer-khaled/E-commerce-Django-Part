from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from utils.query_params import handle_query_params
from django.core.exceptions import ValidationError
from rest_framework import status
from .serializers import CategorySerializer, CategoryCreateSerializer, CategoryUpdateSerializer
from rest_framework import status
from rest_framework.views import APIView
from products.models import Product

class CategoryListView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        params = request.query_params.copy()
        search_fields = ['name']

        if 'category_id' in params and params['category_id'] == '':
            del params['category_id']
        
        try:
            result = handle_query_params(queryset, params, search_fields)
            serializer = CategorySerializer(result['data'], many=True)
            response_data = {
                'categories': serializer.data,
                'current_page': result['current_page'],
                'total_pages': result['total_pages'],
                'total_count': result['total_count']
            }
            return Response(response_data)
        except ValidationError as e:
            return Response({'error': str(e)}, status=400)
        
    def post(self, request):
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class CategoryDetailsView(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)


class AddCategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCategoryView(APIView):
    def delete(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)

            Product.objects.filter(category=category).delete()

            category.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)


