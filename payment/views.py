import os
from dotenv import load_dotenv
import stripe
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from django.utils import timezone
import pytz

from payment.models import Payment
from shipment.models import Shipment
from order.models import Order
from order_item.models import Order_Item
from products.models import Product
from shopping_cart.models import ShoppingCart
from cart_item.models import CartItem

load_dotenv()
# This is your test secret API key.
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class StripeCheckoutView(APIView):
    def post(self,request):

        '''
        user_id = request.data.user_id
        products = request.data.products
        order_details = request.data.order_details

        egypt_tz = pytz.timezone('Africa/Cairo')
        now = timezone.now().astimezone(egypt_tz)

        total_amount = ////
        total_quantity = ////
        line_items = ///


        1) create payment
        - payment.create(payment_method="card")
        
        2) create shipment
        - shipment.create(
        status:"pending",
        shipment_date: now,
        delievery_date: null
        )
        
        3) create order(user)
        - order.create(
        user_id=user_id,
        order_date= now,
        shipment_id = (created shipment.shipment_id),
        address = order_dtails.address,
        city = order_details.city,
        payment_id = (created payment.payment_id)
        )

        4) add products to order_item
        - loop on products 
        OrderItem.create(
        product_id=product_id,
        order_id=(created_order)
        quantity=quantity,
        price=price
        )

        5) Update products stock

        6) cart_id = ShoppingCart.objects.get(user_id=user_id)

        7) Delete User cart_items
        cart_products = cart_Item.objects.filter(cart_id=cart_id)
        cart_products.delet()
        '''

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        # 'price': 'price_1P1lu8EbT5QdQbCziYor5vNN',
                        'price': 'price_1P1lu8EbT5QdQbCziYor5vNN',
                        'quantity': 2,
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


class TestCheckout(APIView):

    def post(self,request):
        try:
            # request data
            user_id = request.data.user_id
            products = request.data.products
            order_details = request.data.order_details
            
            #implicit values
            total_amount = 0
            total_quantity = 0
            line_items = []

            for product in products:
                total_amount += product.price * product.quantity
                total_quantity += product.quantity
                line_items.append({"price":product.payment_id,"quantity":product.quantity})

            # save local time
            egypt_tz = pytz.timezone('Africa/Cairo')
            now = timezone.now().astimezone(egypt_tz)

            # create payment record 
            payment = Payment.objects.create(payment_method="card")
            payment.save()
            payment_id = payment.id

            # create shipment
            shipment = Shipment.objects.create(status="pending",delivery_date="1970-01-01")
            shipment.save()
            shipment_id = shipment.shipment_id
            print(shipment_id)

            #create order
            order = Order.objects.create(
                user_id=user_id,
                shipment_id=shipment_id,
                payment_id=payment_id,
                order_date=now,
                total_amount=total_amount,
                total_quantity=total_quantity,
                address=order_details.address,
                city=order_details.city
                )
            order.save()

            #create Order_item items & update stock values
            for product in products:
                # create order_item records
                Order_Item.objects.create(
                    product_id=product.product_id,
                    order_id=order.order_id,
                    quantity=product.quantity,
                    product_price=product.price
                    )
                
                # update stock values
                product_to_update = Product.objects.get(product_id=product.product_id)
                product_to_update.stock -= product.quantity
                product_to_update.save()
            
            #delete cart from cart_item
            cart_id = ShoppingCart.objects.get(user_id=user_id)
            cart_items = CartItem.objects.filter(cart_id=cart_id)

            cart_items.delete()
            checkout_session = stripe.checkout.Session.create(
                            line_items=line_items,
                            payment_method_types=['card',],
                            mode='payment',
                            success_url= os.getenv('SITE_URL') + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                            cancel_url= os.getenv('SITE_URL') + '/?canceled=true',
                        )
            return redirect(checkout_session.url)

        except:
            return Response({'error':'Error with your payment'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

