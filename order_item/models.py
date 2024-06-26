from django.db import models
from order.models import Order
from products.models import Product
class Order_Item(models.Model):
    order_item_id = models.AutoField(primary_key=True )
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE ,  db_column ='product_id')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE ,  db_column ='order_id') 
    quantity = models.IntegerField(default=0)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["order_id", "product_id"], name="order_item_composite_key")
        ]




