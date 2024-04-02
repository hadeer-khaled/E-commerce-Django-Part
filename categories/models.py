from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name
