from django.urls import path
from .views import DeleteShoppingCartView

urlpatterns = [
    path('shopping-cart/delete/', DeleteShoppingCartView.as_view(), name='delete-shopping-cart'),
]
