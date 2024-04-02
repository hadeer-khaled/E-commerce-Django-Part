from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from utils.query_params import handle_query_params

class CategoryListView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        params = request.query_params
        search_fields = ['name']
        
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
