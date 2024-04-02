from django.db import models
from django.conf import settings
from users.models import User

class ShoppingCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
