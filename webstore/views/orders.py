'''
The OrderView class retrieves orders for a customer and renders them in an orders.html template.
This code defines an OrderView class that inherits from Django's View class. It handles GET requests for the order view. The GET request retrieves the customer ID from the session, fetches the orders associated with the customer from the Order model, and renders the orders.html template with the orders data. The auth_middleware is imported but not used in the code provided, but it would typically be used to protect the view and ensure only authenticated users can access it.

'''
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from webstore.models.customer import Customer
from django.views import View
from webstore.models.product import Products
from webstore.models.orders import Order
from webstore.middlewares.auth import auth_middleware

# OrderView class, inherits from Django's View class
class OrderView(View):

    # Handles GET requests for the order view
    def get(self, request):
        # Get the customer ID from the session
        customer = request.session.get('customer')
        # Get the orders associated with the customer
        orders = Order.get_orders_by_customer(customer)
        # Render the orders.html template with the orders data and return it as a response
        return render(request, 'orders.html', {'orders': orders})

