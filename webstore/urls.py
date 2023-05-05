# This is a Python code that defines the URL patterns for a Django web application. It imports
# necessary modules such as `admin` and `path` from Django, and various views from the application's
# `views` module. It also imports the `auth_middleware` from the `middlewares` module.
from django.contrib import admin
from django.urls import path
from .views.home import Index , webstore , ProductView
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.static_pages import About, PrivacyPolicy, Licensing, Contact

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('webstore', webstore , name='webstore'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('product/', ProductView.as_view(), name='product'),
     path('about', About.as_view(), name='about'),
    path('privacy-policy', PrivacyPolicy.as_view(), name='privacy_policy'),
    path('licensing', Licensing.as_view(), name='licensing'),
    path('contact', Contact.as_view(), name='contact'),

]
