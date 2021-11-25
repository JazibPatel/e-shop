from django.db import models
from django.db.models.deletion import CASCADE
from store.models.category import Category
from store.models.customer import Customer
from store.models.product import Product
import datetime


# Create your models here.

class Order(models.Model):

    name = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=25, default="")
    pincode = models.CharField(max_length=50, default="")
    locality = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    product = models.ForeignKey(Product, on_delete=CASCADE)
    customer = models.ForeignKey(Customer, on_delete=CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def customer_order(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')


