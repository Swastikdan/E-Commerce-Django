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
# Index View class that handles the main page and cart updates
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
        return redirect('homepage_or_webstore')


    # Get method to redirect the user to the webstore page and display the products and categories
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')

        if categoryID == 'all':
            products = Products.get_all_products()
            is_category_page = True
        else:
            products = Products.get_all_products_by_categoryid(categoryID)
            is_category_page = categoryID is not None

        data = {}
        data['categories'] = categories
        data['is_category_page'] = is_category_page

        if is_category_page:
            data['products'] = products
            return render(request, 'category.html', data)
        else:
            product_id = request.GET.get('product_id')
            if product_id:
                product = Products.get_product_by_id(product_id)
                if product:
                    data['products'] = [product]
                    return render(request, 'index.html', data)

            data['products'] = products
            return render(request, 'index.html', data)

# Function to display the webstore page with products and categories


# ProductView class to handle the individual product page and cart updates for that product
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


