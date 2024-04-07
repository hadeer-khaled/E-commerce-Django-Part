from django.urls import path
from .views import StripeCheckoutView , TestCheckout

urlpatterns = [
    path('create-checkout-session',StripeCheckoutView.as_view()),
    path('test-checkout',TestCheckout.as_view())
]