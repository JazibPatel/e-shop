from django.db import models
from .category import Category


# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=150)
    price = models.FloatField(default=0)
    # category model(database table) we have create different that way we use ForeignKey to connect to table
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    details = models.TextField(
        max_length=1000, default=" ", null=True, blank=True)
    image = models.ImageField(upload_to="image")

    # this will display all product in your html.page and other code impement in view.py
    @staticmethod
    def allproduct():
        return Product.objects.all()

    # this will show all category by using categoryid or category_id(categoryid facting from database)
    # and you have to pass categoryid like this only other wise it will show error
    @staticmethod
    def allproduct_category(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.allproduct()

    @staticmethod
    def product_id(ids):

        return Product.objects.filter(id__in=ids)
