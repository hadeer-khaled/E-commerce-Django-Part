from django.urls import path
from .views import ProductListView, ProductDetailsView, ProductImagesView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:product_id>/', ProductDetailsView.as_view(), name='product-details'),
    path('<int:product_id>', ProductDetailsView.as_view(), name='product-details'),
    path('<int:product_id>/images/', ProductImagesView.as_view(), name='product-images'),
    path('<int:product_id>/images', ProductImagesView.as_view(), name='product-images'),
]
