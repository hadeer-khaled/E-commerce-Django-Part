from django.db import models
from django.core.validators import validate_email , MinLengthValidator
from django.core.validators import RegexValidator

validate_phone = RegexValidator(regex='^01[0125][0-9]{8}$', message="Wrong phone number format [Enter Egyptian number]")
roles = (('user','User'),('admin','Admin'))

# Create your models here.
class User (models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    username = models.CharField(max_length=15 , unique=True, validators=[MinLengthValidator(3)])
    email = models.CharField(max_length=50 , unique=True , validators=[validate_email])
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])
    role = models.CharField(choices=roles,max_length=5)
    phone = models.CharField(max_length=11,validators=[validate_phone])
    user_img = models.ImageField()