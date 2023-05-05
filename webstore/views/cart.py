'''
The Cart class handles the functionality of adding and removing products from the cart and
displaying the cart on the cart.html page.


The code above provides a Django view called Cart that handles the rendering and modification of a shopping cart page. The view has two methods: get and post. The get method retrieves the list of products in the cart and renders the cart page with the list of products. The post method handles the addition or removal of products in the cart based on the user's actions.

'''

# Import necessary modules and classes
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from webstore.models.customer import Customer
from django.views import View
from webstore.models.product import Products
from django.http import JsonResponse

# Import necessary modules for handling the Cart page
from django.shortcuts import render, redirect
from django.views import View
from webstore.models.product import Products

# Cart class that handles the cart page rendering and modification
class Cart(View):

    # Get method to render the cart page with the list of products in the cart
    def get(self, request):
        # Retrieve the product ids from the session cart
        ids = list(request.session.get('cart').keys())
        # Get the products corresponding to the ids from the database
        products = Products.get_products_by_id(ids)
        # Render the cart page with the list of products
        return render(request, 'cart.html', {'products': products})

    # Post method to handle the addition or removal of products in the cart
    def post(self, request):
        # Get the product id from the submitted form
        product_id = request.POST.get('product')
        # Get the current cart from the session
        cart = request.session.get('cart')
        
        # Check if the cart exists
        if cart:
            # Get the current quantity of the product in the cart
            quantity = cart.get(product_id)
            # Check if the product is already in the cart
            if quantity:
                # If the remove button is clicked
                if request.POST.get('remove'):
                    # If the product quantity is 1, remove the product from the cart
                    if quantity <= 1:
                        cart.pop(product_id)
                    # Otherwise, decrease the product quantity by 1
                    else:
                        cart[product_id] = quantity - 1
                # If the add button is clicked, increase the product quantity by 1
                else:
                    cart[product_id] = quantity + 1
            # If the product is not in the cart, add it with a quantity of 1
            else:
                cart[product_id] = 1
        # If the cart does not exist, create a new cart with the product and a quantity of 1
        else:
            cart = {product_id: 1}

        # Update the session cart with the modified cart
        request.session['cart'] = cart
        # Redirect the user to the cart page
        return redirect('cart')

