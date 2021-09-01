from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

from accounts.decorators import allowed_groups
from store.models import Product, Order, OrderItem


def get_lading_page(request):
    return render(request, 'store/lading_page.html')


@login_required
@allowed_groups(['user'])
def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        order_items = order.get_order_items
    else:
        items = []
        order = {'get_order_items': 0, 'get_order_total': 0}
        order_items = order['get_order_items']

    products = Product.objects.all()
    context = {'products': products, 'order_items': order_items}
    return render(request, 'store/store_page.html', context=context)


@login_required
@allowed_groups(['user'])
def order(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
        order_items = order.get_order_items
    else:
        items = []
        order = {'get_order_items': 0, 'get_order_total': 0}
        order_items = order['get_order_items']

    context = {'items': items, 'order': order, 'order_items': order_items}
    return render(request, 'store/order_page.html', context=context)


@login_required
@allowed_groups(['user'])
def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)

