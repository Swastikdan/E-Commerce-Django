"""
The above code defines views for the webstore app, including an index view, a product view, and a
webstore view.
    
:param request: The request object represents the current HTTP request that is being processed by
the server
:return: It is not clear which function or view is being referred to, so it is not possible to
determine what is being returned.

The code above provides three views for a webstore application: Index, webstore, and ProductView.

Index class handles the main page and cart updates. It has a post method for updating the cart when a user adds or removes a product, and a get method to redirect the user to the webstore page.

webstore is a function that displays the webstore page with products and categories. It retrieves the categories and products based on the selected category or displays all products if no category is selected. It then renders the index.html template with the products and categories data.

ProductView class handles individual product pages and cart updates for specific products. The get method displays the individual product page based on the product ID, and the post method updates the cart when the user adds or removes a product from the individual product page. After updating the cart, the user is redirected back to the same product page.
    """
from django.shortcuts import render, redirect, HttpResponseRedirect
from webstore.models.product import Products
from webstore.models.category import Category
from django.views import View
from django.contrib.auth.hashers import check_password
from webstore.models.customer import Customer
from django.views import View
from webstore.models.product import Products
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
# Index View class that handles the main page and cart updates
# The Index class handles cart updates and displays all products on the webstore page.
class Index(View):
    # Post method to handle cart updates (add/remove product)
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        # Update the cart based on the add/remove action
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        # Update the session cart
        request.session['cart'] = cart

        # Get the category ID of the product
        product_category = Products.objects.get(id=product).category_id

        # Redirect to the category page with the updated query
        return redirect('category', category_id=product_category)


    # Get method to redirect the user to the webstore page and display all products
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        categories = Category.objects.all()
        products = Products.objects.all()

        data = {
            'categories': categories,
            'is_category_page': False,
            'products': products,
            'cart': cart  # Add the 'cart' data to the template context
        }

        return render(request, 'index.html', data)



# This is a class-based view that displays products belonging to a specific category and raises a 404
# error if the category is not found.
class CategoryView(View):
    def get(self, request, category_id):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        categories = Category.objects.all()
        products = Products.objects.filter(category_id=category_id)
        category = Category.objects.get(id=category_id)

        if not products:
            raise Http404("Category not found.")

        data = {
            'categories': categories,
            'is_category_page': True,
            'products': products,
            'category': category
        }

        return render(request, 'category.html', data)




# ProductView class to handle the individual product page and cart updates for that product
# The ProductView class handles GET and POST requests for individual product pages, including updating
# the cart.
class ProductView(View):
    def get(self, request):
        product_id = request.GET.get('id')
        if product_id:
            product = get_object_or_404(Products, id=product_id)
            return render(request, 'product.html', {'product': product})
        else:
            return redirect('homepage_or_webstore')
    # Post method to handle cart updates (add/remove product) from the individual product page
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        # Update the cart based on the add/remove action
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        

        # Update the session cart and redirect to the same product page
        request.session['cart'] = cart
        return HttpResponseRedirect(request.path + "?id=" + product)


