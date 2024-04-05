from django.contrib import admin
from django.urls import path ,include
from .views import insert_dummy_data_view
from categories.views import CategoryListView
from products.views import ProductListView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('insert-dummy-data/', insert_dummy_data_view, name='insert_dummy_data'),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('categories/', include('categories.urls')),
    path('categories', CategoryListView.as_view(), name='category-list'),
    path('products/', include('products.urls')),
    path('orders/',include("order.urls")),
    path('products', ProductListView.as_view(), name='product-list'),
    path('wishlist/',include('wishlist.urls')),
    path('orders/',include("order.urls")),
    path('payment/',include('payment.urls'))
    path('shoppingCart/',include('shopping_cart.urls')),
    path('cartItem/',include('cart_item.urls')),
    ] +static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
