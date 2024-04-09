from django.urls import path
from .views import AddToCartView, ViewCartItems,IncrementCartItemQuantityView, DecrementCartItemQuantityView,RemoveFromCartView

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add-to-cart'),
    path('view-cart/', ViewCartItems.as_view(), name='view-cart'),
    path('increment-quantity/', IncrementCartItemQuantityView.as_view(), name='increment-quantity'),
    path('decrement-quantity/', DecrementCartItemQuantityView.as_view(), name='decrement-quantity'),
    path('remove-from-cart/', RemoveFromCartView.as_view(), name='remove_from_cart'),

]
