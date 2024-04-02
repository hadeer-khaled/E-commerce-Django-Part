from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, ProductImage
from .serializers import ProductSerializer
from utils.query_params import handle_query_params
from django.core.exceptions import ValidationError

class ProductListView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        params = request.query_params
        search_fields = ['name']
        
        try:
            result = handle_query_params(queryset, params, search_fields)
            serializer = ProductSerializer(result['data'], many=True)
            response_data = {
                'products': serializer.data,
                'current_page': result['current_page'],
                'total_pages': result['total_pages'],
                'total_count': result['total_count']
            }
            return Response(response_data)
        except ValidationError as e:
            return Response({'error': str(e)}, status=400)

class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
        
class ProductImagesView(APIView):
    def get(self, request, product_id):
        product_images = ProductImage.objects.filter(product_id=product_id)
        print(product_images)
        image_urls = [image.image.url for image in product_images]
        return Response(image_urls)
