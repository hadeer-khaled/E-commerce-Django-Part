from django.urls import path
from .views import DeleteShoppingCartView

urlpatterns = [
    path('delete/', DeleteShoppingCartView.as_view(), name='delete-shopping-cart'),
]
