from django.db import models
from users.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
