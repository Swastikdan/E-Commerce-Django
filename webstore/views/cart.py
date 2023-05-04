from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from webstore.models.customer import Customer
from django.views import  View
from webstore.models.product import Products

from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.views import View
from webstore.models.product import Products

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})

    def post(self, request):
        product_id = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if request.POST.get('remove'):
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity - 1
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {product_id: 1}

        request.session['cart'] = cart
        return redirect('cart')


