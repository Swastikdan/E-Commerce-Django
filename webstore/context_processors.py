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

# def cart_items(request):
#     cart = request.session.get('cart', {})
#     cart_items = []
#     total_price = 0

#     for product_id, quantity in cart.items():
#         product = Products.objects.get(id=product_id)
#         cart_items.append({
#             'name': product.name,
#             'price': product.price,
#             'image': product.image.url,
#             'quantity': quantity
#         })
#         total_price += product.price * quantity

#     return {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     }
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
