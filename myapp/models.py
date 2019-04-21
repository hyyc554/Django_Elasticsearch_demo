from django.db import models

# Create your models here.


class Goods(models.Model):
    id = models.IntegerField(primary_key=True
    )
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
