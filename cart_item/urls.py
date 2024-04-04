from django.urls import path
from .views import AddToCartView, ViewCartItems

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('view-cart/', ViewCartItems.as_view(), name='view-cart'),
]
