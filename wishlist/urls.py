from django.urls import path
from .views import WishlistListView, AddToWishlistView, RemoveFromWishlistView

urlpatterns = [
    path('', WishlistListView.as_view(), name='wishlist-list'),
    path('wishlist/add/', AddToWishlistView.as_view(), name='add-to-wishlist'),
    path('wishlist/remove/', RemoveFromWishlistView.as_view(), name='remove-from-wishlist'),
]
