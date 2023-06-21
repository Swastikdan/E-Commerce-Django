
"""
    The function retrieves customer information, categories, and cart items with their respective
    quantities and prices.
    
    :param request: The HTTP request object that contains information about the current request
    :return: The code is returning a dictionary containing the customer information, categories, and
    cart items with their respective details such as name, price, image, and quantity. The total price
    of all the items in the cart is also included in the dictionary. If the cart is empty, a flag
    'cart_empty' is added to the dictionary.
"""
from .models import Customer, Products , Category
def customer_info(request):
    customer = None
    if request.session.get('customer'):
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id=customer_id)
    return {'customer': customer}


def categories(request):
    categories = Category.get_all_categories()
    return {'categories': categories}


def cart_items(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = Products.objects.get(id=product_id)
        cart_items.append({
            'name': product.name,
            'price': product.price,
            'image': product.image.url,
            'quantity': quantity
        })
        total_price += product.price * quantity

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    if not cart_items:
        context['cart_empty'] = True

    return context
