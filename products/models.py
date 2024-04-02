from django.db import models
from categories.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.CharField(max_length=255)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    image = models.ImageField(upload_to='uploads/product_images/')

    def __str__(self):
        return self.name
