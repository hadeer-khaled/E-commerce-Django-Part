from django.urls import path
from .views import CategoryListView, CategoryDetailsView


urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('<int:category_id>/', CategoryDetailsView.as_view(), name='category-details'),
]
