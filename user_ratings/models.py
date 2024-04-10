from django.db import models
from users.models import User
from products.models import Product


class user_ratings(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column ='user_id')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE ,  db_column ='product_id')
    rating = models.IntegerField(default=0)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user_id", "product_id"], name="rating_composite_key")
        ]
