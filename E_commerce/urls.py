from django.contrib import admin
from django.urls import path ,include
from .views import insert_dummy_data_view

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('insert-dummy-data/', insert_dummy_data_view, name='insert_dummy_data'),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('orders/',include("order.urls")),
    path('orderitem/',include("order_item.urls")),
    ] +static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
