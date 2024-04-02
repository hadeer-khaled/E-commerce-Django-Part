from django.contrib import admin
from django.urls import path ,include
from .views import insert_dummy_data_view
from categories.views import CategoryListView
from products.views import ProductListView, ProductImagesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('insert-dummy-data/', insert_dummy_data_view, name='insert_dummy_data'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:product_id>/images/', ProductImagesView.as_view(), name='product-images'),
    # path('order/',include("order.urls"))
]
