from django.urls import path
# now we have create views folder that way we have to change the method of view of templates
# instant of ( from home import views )
from .views.home import Home
from .views.singup import Singup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import Checkout
from .views.order import ViewOrder
from .middlewares.auth import auth_middleware

urlpatterns = [
    # instand of ( path('', views.home, name="home"), ) because we have use class in views file
    path('', Home.as_view(), name="home"),
    path('singup', Singup.as_view(), name="singup"),
    path('login', Login.as_view(), name="login"),
    path('logout', logout, name="logout"),
    # path('cart', Cart.as_view(), name="cart"),
    path('checkout', Checkout.as_view(), name="checkout"),
    path('order', ViewOrder.as_view(), name="order"),
    path('cart', auth_middleware(Cart.as_view()), name="cart"),
] 
