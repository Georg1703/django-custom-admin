from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib import messages
import json

from accounts.decorators import allowed_groups
from store.models import Product, Order, OrderItem
from .forms import OrderTicketForm


def get_lading_page(request):
    return render(request, 'store/lading_page.html')


@login_required
@allowed_groups(['user'])
def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, placed=False)
        order_items = order.get_order_items
    else:
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
        order, created = Order.objects.get_or_create(customer=customer, placed=False)
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
    order, created = Order.objects.get_or_create(customer=customer, placed=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    is_deleted = False

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
        order_item.save()
    elif action == 'down':
        order_item.quantity = (order_item.quantity - 1)
        order_item.save()
    elif action == 'remove':
        order_item.delete()
        is_deleted = True

    if order_item.quantity <= 0:
        order_item.delete()
        is_deleted = True

    context = {
        'quantity': order_item.quantity,
        'total_quantity': order.get_order_items,
        'get_order_total': order.get_order_total,
        'product_total_price': order_item.get_total,
        'is_deleted': is_deleted,
        'product_id': product_id,
    }
    return JsonResponse(context)


@login_required
@allowed_groups(['user'])
def place_order(request, order_id):

    if request.user.is_authenticated:
        order = Order.objects.get(id=order_id)
        if order.orderitem_set.count() > 0:
            order.placed = True
            order.save()
            messages.success(request, 'Order was placed !')
            return redirect('/order')
        else:
            messages.success(request, 'Order is empty !')
            return redirect('/order')
    else:
        messages.success(request, 'Order was not placed !')
        return redirect('/order')


@login_required
@allowed_groups(['user'])
def order_history(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, placed=True).all()
    else:
        order = {'get_order_items': 0, 'get_order_total': 0}

    context = {'orders': order}
    return render(request, 'store/order_history.html', context=context)


@login_required
@allowed_groups(['user'])
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderTicketForm()
    context = {'order': order}

    if request.method == 'POST':
        form = OrderTicketForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Comment was saved !')
            return redirect('store:order_detail')
        else:
            messages.success(request, 'Error!')
            context['form'] = form
            return render(request, 'store/order_detail.html', context)
    else:
        context['form'] = form
        return render(request, 'store/order_detail.html', context)

