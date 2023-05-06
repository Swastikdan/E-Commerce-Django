# views/__init__.py
from .home import Index, webstore, ProductView
from .signup import Signup
from .login import Login, logout
from .cart import Cart
from .checkout import CheckOut
from .orders import OrderView
from .static_pages import About, PrivacyPolicy, Licensing,  Service
from .contact import ContactView 