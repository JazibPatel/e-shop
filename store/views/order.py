# instand of views.py we have create saprat folder for views like models
# in this folder different file.py for different models & html.page

from django.shortcuts import redirect, render

# to use class in view we have to impor this
from django.views import View
from store.models.category import Category
from store.models.order import Order

from store.models.product import Product
from store.models.customer import Customer

# Create your views here.

# instant def diractly we have creat class and in class two methods 
# this method handel by it self like if else
class ViewOrder(View):

    def get(self, request):
        customer = request.session.get('customer_id')
        order = Order.customer_order(customer)
        # print("order",order)
        order = reversed(order)
        return render(request, "order.html", {'orders':order})