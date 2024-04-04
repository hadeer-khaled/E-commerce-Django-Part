from django.urls import path
from .views import OrderItemDetailView 

urlpatterns = [
    path('', OrderItemDetailView.as_view()),

]