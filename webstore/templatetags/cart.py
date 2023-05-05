
# This is a set of Django template filters that help with displaying and calculating cart-related
# information for an e-commerce website.
    
# :param product: an instance of a product model in Django
# :param cart: A dictionary containing the products in the user's cart and their quantities. The keys
# are the product IDs and the values are the quantities
# :return: The code defines four custom template filters for a Django web application related to a
# shopping cart.

from django import template
register = template.Library ()


@register.filter (name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return True
    return False


@register.filter (name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return cart.get (id)
    return 0


@register.filter (name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity (product, cart)


@register.filter (name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total (p, cart)

    return sum
