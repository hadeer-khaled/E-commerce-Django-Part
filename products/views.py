from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, ProductImage, Category
from utils.query_params import handle_query_params
from django.core.exceptions import ValidationError
from .serializers import ProductSerializer, ProductCreateSerializer, ProductUpdateSerializer, ProductImageSerializer
from rest_framework import status

class ProductListView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        params = request.query_params.copy()
        search_fields = ['name']

        if 'product_id' in params and params['product_id'] == '':
            del params['product_id']
        if 'category' in params and params['category'] == '':
            del params['category']

        try:
            result = handle_query_params(queryset, params, search_fields)
            products_data = []
            for product in result['data']:
                product_data = get_product_details(product.product_id)
                products_data.append(product_data)
                
            response_data = {
                'products': products_data,
                'current_page': result['current_page'],
                'total_pages': result['total_pages'],
                'total_count': result['total_count']
            }
            return Response(response_data)
        except ValidationError as e:
            return Response({'error': str(e)}, status=400)
        
    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product_data = get_product_details(product_id)
            return Response(product_data)
        except ValidationError as e:
            return Response({"error": str(e)}, status=404)
    
    def put(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductUpdateSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ProductImagesView(APIView):
    def get(self, request, product_id):
        image_urls = get_image_urls(product_id)
        return Response(image_urls)
    
    def post(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_image_urls(product_id):
    product_images = ProductImage.objects.filter(product_id=product_id)
    image_urls = [image.image.url for image in product_images]
    return image_urls

def get_category(category_id):
    category = Category.objects.filter(category_id=category_id)
    category_name = category[0].name
    return category_name

def get_product_details(product_id):
    try:
        product = Product.objects.get(pk=product_id)
        image_urls = get_image_urls(product_id)
        category_name = get_category(product.category.category_id)
      
        product_data = {
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,
            "description": product.description,
            "avg_rating": product.avg_rating,
            "category": category_name,
            "images": image_urls,
            "payment_id": product.payment_id
        }
        return product_data
    except Product.DoesNotExist:
        raise ValidationError("Product not found")

