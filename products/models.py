from django.db import models
from categories.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator

def upload_to(instance, filename):
    return 'products_images/{filename}'.format(filename=filename)



class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.CharField(max_length=255)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    image = models.CharField(max_length=200, default='products_images/default_product.png')
    # payment_id = models.CharField(max_length=100, unique=True, default="")

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/uploads/product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
