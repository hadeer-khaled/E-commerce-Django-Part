import os
from dotenv import load_dotenv
import stripe
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from django.utils import timezone
import pytz

from users.models import User
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
            products = request.data['products']
            
            #implicit values
            total_amount = 0
            total_quantity = 0
            line_items = []

            for product in products:
                total_amount =  total_amount + (float(product['price']) * int(product['quantity']))
                total_quantity = total_quantity + int(product['quantity'])
                line_items.append({"price":product['payment_id'],"quantity":product['quantity']})

            print("Line Items", line_items)
            
            checkout_session = stripe.checkout.Session.create(
                        line_items=line_items,
                        payment_method_types=['card',],
                        mode='payment',
                        success_url= os.getenv('SITE_URL') + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                        cancel_url= os.getenv('SITE_URL') + '/?canceled=true',
                    )
            # print("Chcekout session", checkout_session.url)
            return Response({"url": checkout_session.url})
            


        except:
            return Response({'error':'Error with your payment'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ConfirmPayment(APIView):

        def post(self,request):
                #request data
                products = request.data['products']
                user_id = request.data['user_id']
                order_details = request.data['order_details'] 

                #implicit values
                total_amount = 0
                total_quantity = 0

                for product in products:
                    total_amount = total_amount + (float(product['price']) * int(product['quantity']))
                    total_quantity = total_quantity + int(product['quantity'])           

                # save local time
                egypt_tz = pytz.timezone('Africa/Cairo')
                now = timezone.now().astimezone(egypt_tz)

                # create payment record 
                payment = Payment.objects.create(payment_method="card")
                payment.save()

                # create shipment
                shipment = Shipment.objects.create(status="pending",delivery_date=now)
                shipment.save()

                #get user
                user = User.objects.get(user_id=user_id)

                #create order
                order = Order.objects.create(
                    user_id=user,
                    shipment_id=shipment,
                    payment_id=payment.id,
                    order_date=now,
                    total_amount=total_amount,
                    total_quantity=total_quantity,
                    address=order_details['address'],
                    city=order_details['city']
                    )
                order.save()

                #create Order_item items & update stock values
                for product in products:
                    # create order_item records
                    item = Order_Item.objects.create(
                        product_id=product['product_id'],
                        order_id=order,
                        quantity=product['quantity'],
                        product_price=product['price']
                        )
                    item.save()
                    
                    # update stock values
                    product_to_update = Product.objects.get(product_id=product['product_id'])
                    product_to_update.stock = product_to_update.stock - product['quantity']
                    product_to_update.save()
                
                #delete cart from cart_item
                cart_id = ShoppingCart.objects.get(user_id=user_id)
                cart_items = CartItem.objects.filter(cart_id=cart_id)

                cart_items.delete()
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa")
                # return redirect(checkout_session.url)
                return Response({"message":"Order created successfully !!"})
