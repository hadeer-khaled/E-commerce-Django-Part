from django.contrib import admin
from django.urls import path ,include
from .views import insert_dummy_data_view

urlpatterns = [
    path('insert-dummy-data/', insert_dummy_data_view, name='insert_dummy_data'),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    # path('order/',include("order.urls"))
]
