'''
The CheckOut class handles the post request for placing an order and saves the order details in the
database.

The code above provides a Django view called CheckOut that handles the checkout process and order creation. The view has a post method that handles the submission of the checkout form, which includes the customer's address, phone number, and the cart's contents. When the form is submitted, the post method iterates through the products in the cart, creates a new Order object for each product, and saves it to the database. After the orders have been created, the session cart is cleared, and the user is redirected to the cart page.

'''

# Import necessary modules and classes
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from webstore.models.customer import Customer
from django.views import View
from webstore.models.product import Products
from webstore.models.orders import Order

# CheckOut class that handles the checkout process and order creation
class CheckOut(View):

    # Post method to handle the checkout form submission and create orders
    def post(self, request):
        # Get the submitted address, phone, and customer information from the form
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        # Get the current cart from the session
        cart = request.session.get('cart')
        # Get the products corresponding to the ids from the cart
        products = Products.get_products_by_id(list(cart.keys()))
        
        # Iterate through the products in the cart
        for product in products:
            # Get the quantity of the current product in the cart
            quantity = cart.get(str(product.id))
            # Create a new Order object with the submitted information and product details
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=quantity)
            # Save the Order object to the database
            order.save()

        # Clear the session cart after the order has been created
        request.session['cart'] = {}

        # Redirect the user to the cart page
        return redirect('cart')

