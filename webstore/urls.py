from django.contrib import admin
from django.urls import path
from .views.home import Index , webstore , ProductView ,handle_404 , handle_500
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView

from .middlewares.auth import  auth_middleware

handler404 = handle_404
handler500 = handle_500
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
    path('404/', handle_404, name='404'),
    path('500/', handle_500, name='500'),
]
