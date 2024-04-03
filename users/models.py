from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

roles = (('user','User'),('admin','Admin'))

class UserManager(BaseUserManager):

    def create_user(self,email,password,first_name,last_name,phone,role):
        if not email:
            raise ValueError("Email is required.")
        if not password:
            raise ValueError("Email is required.")
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name,phone=phone,role=role)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email , password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required.")

        if not password:
            raise ValueError("Email is required.")

        user = self.create_user(email,password,phone="",role="admin",**extra_fields)
        user.is_superuser = True
        user.role = "admin"
        user.save()
        return user
    
# Create your models here.
class User (AbstractUser,PermissionsMixin):

        user_id = models.BigAutoField(primary_key=True)
        first_name = models.CharField(max_length=20)
        last_name = models.CharField(max_length=20)
        username = models.CharField(max_length=15,unique=True)
        email = models.CharField(max_length=50,unique=True)
        password = models.CharField(max_length=100)
        role = models.CharField(choices=roles,max_length=5)
        phone = models.CharField(max_length=11)
        image = models.ImageField( blank=True , upload_to='users_images/'  , default='users_images/default.png')
        objects = UserManager()

        USERNAME_FIELD= 'email'
        REQUIRED_FIELDS=['first_name','last_name']

        def __str__(self):
                return self.first_name + " " + self.last_name