from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from shopping_cart.models import ShoppingCart
from products.models import Product

# Create your models here.
class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
