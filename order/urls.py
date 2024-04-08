from django.urls import path
from .views import AllOrdersView , SpecificOrderView, SpecificUserOrdersView
from order_item.views import OrderItemDetailView
urlpatterns = [
    path('', AllOrdersView.as_view()),
    path('order/<int:order_id>/', SpecificOrderView.as_view()),
    path('order/<int:order_id>/order_items', OrderItemDetailView.as_view()),
    # path('userorder/<int:user_id>/', SpecificUserOrdersView.as_view()),
    ]