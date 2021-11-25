# instand of views.py we have create saprat folder for views like models
# in this folder different file.py for different models & html.page

from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render
from store.models.customer import Customer
from django.http import HttpResponseRedirect

# to use class in view we have to impor this
from django.views import View

# Create your views here.

# instant def diractly we have creat class and in class two methods 
# this method handel by it self like if else

class Login(View):
    
    return_url = None
     # it like [ if request.method == "GET": ] as simple as that
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, "login.html")

     # it like [ if request.method == "POST": ] as simple as that
    def post(self, request):

        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.User_Email(email)

        # this message is pass for passing message in html.page 
        message = None
        if customer:
            user = check_password(password, customer.password)
            if user:
                request.session['customer_id'] = customer.id
                message = "LogIn Succesfull"
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect("home")
            else:
                message = "Email or Password Is Invalid!!!"
                return render(request, "login.html",{'message':message})
        else:
            message = "Invalid User!!!"
        return render(request, "login.html",{'message':message})

def logout(request):
    request.session.clear()
    return redirect("home")

