from django.urls import path
from .views import WishlistListView, WishlistDetailView, AddToWishlistView, RemoveFromWishlistView

urlpatterns = [
    path('', WishlistListView.as_view(), name='wishlist-list'),
    path('wishlist/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('wishlist/add/', AddToWishlistView.as_view(), name='add-to-wishlist'),
    path('wishlist/remove/<int:wishlist_item_id>/', RemoveFromWishlistView.as_view(), name='remove-from-wishlist'),
]
