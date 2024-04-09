from django.urls import path
from .views import StripeCheckoutView , TestCheckout , ConfirmPayment

urlpatterns = [
    path('create-checkout-session',StripeCheckoutView.as_view()),
    path('test-checkout',TestCheckout.as_view()),
    path('confirm',ConfirmPayment.as_view())
]