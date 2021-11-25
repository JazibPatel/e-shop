from django.contrib import admin

# Register your models here.

# we have create folder of models thay way he have to 
# import from folder(models) 
# then from file(__init__.py) 
# then import models name

from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order

# this class is use to display your database table by your chooise
class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['id','firstname', 'lastname', 'email']

class AdminOrder(admin.ModelAdmin):
    list_display = ['name', 'product', 'date', 'status']
# Register your models here.


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
