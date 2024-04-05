import os
from dotenv import load_dotenv
import stripe
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

load_dotenv()
# This is your test secret API key.
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class StripeCheckoutView(APIView):
    def post(self,request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1P1lu8EbT5QdQbCziYor5vNN',
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card',],
                mode='payment',
                success_url= os.getenv('SITE_URL') + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= os.getenv('SITE_URL') + '/?canceled=true',
            )
            
            return redirect(checkout_session.url)

        except:
            return Response({'error':'Error with your payment'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


