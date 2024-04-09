from django.db import models
from users.models import User
class Shipment(models.Model):
    stauts_choices = [ ("pending","pending") , ("shipped" ,"shipped") ,("delivered" ,"delivered")]

    shipment_id =models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE ,  db_column ='user_id') 
    # order_id = models.ForeignKey(Order, on_delete=models.CASCADE ,  db_column ='order_id') 
    status = models.CharField(max_length = 10,choices = stauts_choices , default = "pending" )
    delivery_date = models.DateTimeField()

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=["user_id", "order_id"], name="shipment_composite_key")]