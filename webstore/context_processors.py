from .models import Customer

def customer_info(request):
    customer = None
    if request.session.get('customer'):
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id=customer_id)

    return {'customer': customer}
