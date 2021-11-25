# instand of views.py we have create saprat folder for views like models
# in this folder different file.py for different models & html.page

from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category

# to use class in view we have to impor this
from django.views import View

# Create your views here.

# instant def diractly we have creat class and in class two methods 
# this method handel by it self like if else
class Home(View):
    
    # it like [ if request.method == "GET": ] as simple as that
    def get(self,request):

        cart = request.session.get('cart')
        if not cart:

            request.session['cart'] = {}

        product = None
        # allcategory function define in category.py
        category = Category.allcategory()
        categoryID = request.GET.get('category')

        if categoryID:
            # allproduct_category function define in product.py
            product = Product.allproduct_category(categoryID)
        else:
            # allproduct function define in product.py
            product = Product.allproduct()

        # data is empty distneroy becaues in render 3 position is for distneroy 
        # and it take 1 distneroy only that way product & category define in data
        data = {}
        data['products'] = product
        data['categorys'] = category
        return render(request, "home.html", data)

    # it like [ if request.method == "POST": ] as simple as that
    
    def post(self, request):
        
        # this product is defind in home.html in form to get product id 
        product = request.POST.get('product')
        # print("Product Id : ",product)

        if product is None:
            return redirect("home")

        # remove define in home.html to remove product from cart        
        remove = request.POST.get('remove')

        # this is also defind in login.py to get email or user and store in session
        # print("You are : ",request.session.get('email'))
        

        # cart is just an object or varibal to store product and its quantity
        cart = request.session.get('cart')
        # cart = {}
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # print("Cart : ",request.session['cart'])
        return redirect("home")