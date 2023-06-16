# views/__init__.py
from .home import Index,  ProductView , CategoryView
from .signup import Signup
from .login import Login, logout
from .cart import Cart
from .checkout import CheckOut
from .orders import OrderView
from .static_pages import About, PrivacyPolicy,  Service ,faq , custom_404 ,custom_500
from .contact import ContactView 