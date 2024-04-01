from django.db import models
from shipment.models import Shipment
from django.utils import timezone
from users.models import User


class Order(models.Model):
    order_id = models.AutoField(primary_key=True , default=0)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE , db_column ='user_id')
    order_date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_quantity	  = models.IntegerField()
    shipment_id = models.OneToOneField(Shipment, on_delete=models.CASCADE , db_column ='shipment_id')
    address	      = models.CharField(max_length =100)
    city	 = models.CharField(max_length =30)
    payment_id   = models.IntegerField() 
    # payment_id = models.OneToOneField(Payment, on_delete=models.CASCADE)

     


    # class Meta:
    #     verbose_name = "Order"
    #     ordering = ['-order_id']
