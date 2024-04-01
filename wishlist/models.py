from django.db import models
from users.models import User

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # products = models.ForeignKey(Product, related_name='wishlists')

    def __str__(self):
        return f"Wishlist {self.wishlist_id} - User: {self.user.username}"