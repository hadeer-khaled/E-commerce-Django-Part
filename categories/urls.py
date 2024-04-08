from django.urls import path
from .views import CategoryListView, CategoryDetailsView,AddCategoryView,DeleteCategoryView


urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('<int:category_id>/', CategoryDetailsView.as_view(), name='category-details'),
    path('<int:category_id>', CategoryDetailsView.as_view(), name='category-details'),
    path('add/', AddCategoryView.as_view(), name='add-category'),
    path('delete/<int:category_id>/', DeleteCategoryView.as_view(), name='delete-category'),
]
