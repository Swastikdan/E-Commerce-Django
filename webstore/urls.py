# This is a Python code that defines the URL patterns for a Django web application. It imports
# necessary modules such as `admin` and `path` from Django, and various views from the application's
# `views` module. It also imports the `auth_middleware` from the `middlewares` module.
from django.contrib import admin
from django.urls import path
from .views import Index, ProductView, Signup, Login, logout, Cart, CheckOut, OrderView, About, PrivacyPolicy,  Service, ContactView ,faq ,custom_404 ,custom_500 ,CategoryView
from django.urls import path


from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage_or_webstore'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('login/', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('product/', ProductView.as_view(), name='product'),
    path('about', About.as_view(), name='about'),
    path('privacy-policy', PrivacyPolicy.as_view(), name='privacy_policy'),
    path('services', Service.as_view(), name='services'),
    path('contact', ContactView.as_view(), name='contact'), 
    path('faq', faq.as_view(), name='faq'),
    path('product/', ProductView.as_view(), name='productview'),
    path('category/<int:category_id>', CategoryView.as_view(), name='category'),

]
handler404 = custom_404
# `handler500 = custom_500` is assigning the `custom_500` function from the current module to the
# `handler500` variable. This is used to specify a custom view function to handle server errors (HTTP
# 500 responses) in the Django application. When an error occurs, Django will call the `custom_500`
# function to handle the error and generate an appropriate response.
handler500 = custom_500

