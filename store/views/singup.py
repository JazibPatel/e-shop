# instand of views.py we have create saprat folder for views like models
# in this folder different file.py for different models & html.page

from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from store.models.customer import Customer

# to use class in view we have to impor this
from django.views import View

# Create your views here.

# instant def diractly we have creat class and in class two methods 
# this method handel by it self like if else

class Singup(View):
    
    # it like [ if request.method == "GET": ] as simple as that
    def get(self, request):
        return render(request, "singup.html")

    # it like [ if request.method == "POST": ] as simple as that
    def post(self, request):

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer(firstname=firstname,
                            lastname=lastname,
                            phone=phone,
                            email=email,
                            password=make_password(password))

        # this message is pass for passing message in html.page 
        message = None

        # this function is define in customer.py
        # this function check if there is already user are ther or not
        # in if condation model varibale should use aother wise it give error (customer.User_Exists() NOT [Customer.User_Exists()])
        if customer.User_Exists():
            message = "User Already Resigter!!!"
            return render(request, "singup.html", {'message': message})

        else:
            customer.save()
        
        return redirect("home")

