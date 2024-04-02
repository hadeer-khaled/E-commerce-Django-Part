from django.contrib import admin
from django.urls import path ,include
from .views import insert_dummy_data_view
from categories.views import CategoryListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('wishlist/',include('wishlist.urls')),
    path('insert-dummy-data/', insert_dummy_data_view, name='insert_dummy_data'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('order/',include("order.urls"))
]
