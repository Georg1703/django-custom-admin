from .models import Tag, Order


def store_processor(request):
    tags = Tag.objects.all()
    order = {'get_order_items': 0, 'get_order_total': 0}
    items = []

    if request.user.is_authenticated:
        if request.user.groups.filter(name='user').exists():
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, placed=False)
            items = order.orderitem_set.all()

    return {'order': order, 'tags': tags, 'items': items, 'lang': request.LANGUAGE_CODE, 'user': request.user}