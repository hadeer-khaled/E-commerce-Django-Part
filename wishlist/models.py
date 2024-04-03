from django.db import models
from users.models import User
from products.models import Product

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
