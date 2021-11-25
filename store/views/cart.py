# instand of views.py we have create saprat folder for views like models
# in this folder different file.py for different models & html.page

from django.shortcuts import redirect, render
from store.models.product import Product

# from store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator

# to use class in view we have to impor this
from django.views import View

# Create your views here.

# instant def diractly we have creat class and in class two methods 
# this method handel by it self like if else
class Cart(View):

    # @method_decorator(auth_middleware)

    def get(self, request):

        ids = (list(request.session.get('cart').keys()))
        product = Product.product_id(ids)
        # print(product)
        return render(request, "cart.html",{'products':product})
    
    def post(self, request):
        
        # this product is defind in home.html in form to get product id 
        product = request.POST.get('product')
        # print("Product Id : ",product)

        # remove define in home.html to remove product from cart        
        remove = request.POST.get('remove')
        itemremove = request.POST.get('itemremove')
        
        # cart is just an object or varibal to store product and its quantity
        cart = request.session.get('cart')
        # cart = {}
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
                    
                    if itemremove:
                        if quantity:
                            cart.pop(product)
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # print("Cart : ",request.session['cart'])
        return redirect("cart")