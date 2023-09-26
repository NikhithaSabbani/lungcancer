from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    prd_name=models.CharField(max_length=40)
    prd_price=models.IntegerField()
    prd_code=models.BigIntegerField()
    prd_quantity=models.IntegerField()


    def get_absolute_url(self):
        return reverse('display')

