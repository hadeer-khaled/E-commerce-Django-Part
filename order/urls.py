from django.urls import path
from .views import AllOrdersView , SpecificOrderView, SpecificUserOrdersView
urlpatterns = [
    path('', AllOrdersView.as_view()),
    path('order/<int:order_id>/', SpecificOrderView.as_view()),
    path('userorder/<int:user_id>/', SpecificUserOrdersView.as_view()),]