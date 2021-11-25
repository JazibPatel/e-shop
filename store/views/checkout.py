# instand of views.py we have create saprat folder for views like models
# in this folder different file.py for different models & html.page

from django.shortcuts import redirect
import razorpay


# to use class in view we have to impor this
from django.views import View
from razorpay import client

from store.models.category import Category
from store.models.order import Order

from store.models.product import Product
from store.models.customer import Customer


# Create your views here.

# instant def diractly we have creat class and in class two methods 
# this method handel by it self like if else
class Checkout(View):

    
    
    

    def post(self, request):
        import razorpay
        from razorpay import client
        amount = 10
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_NKP3ttSeDQPZSu','8Wq4CZQaepDgM5h8hyvgl1Yi'))
        payment = client.order.create({'amount':amount*100, 'currency':'INR', 'payment_capture':'1'})

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        locality = request.POST.get('locality')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.product_id(list(cart.keys()))
        # print("jazib ",address,phone,customer,cart,products)

        for product in products:
            order = Order(name = name,
                          phone = phone,
                          pincode = pincode,
                          locality = locality,
                          address = address,
                          city = city,
                          state = state,
                          customer = Customer(id = customer),
                          product = product,
                          price = product.price,
                          quantity = cart[str(product.id)])
            order.save()
        
        request.session['cart'] = {}

        

        
        return redirect("home")