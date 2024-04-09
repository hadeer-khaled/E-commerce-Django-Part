from django.db import models
from users.models import User

class Payment(models.Model):
    payment_method = models.CharField(max_length=100)
