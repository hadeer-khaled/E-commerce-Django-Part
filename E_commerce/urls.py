from django.contrib import admin
from django.urls import path ,include
from .views import insert_dummy_data_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('insert-dummy-data/', insert_dummy_data_view, name='insert_dummy_data'),
    # path('order/',include("order.urls"))
]
