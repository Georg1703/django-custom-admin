from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib import messages
from store.models import Tag
import json

from accounts.decorators import allowed_groups
from .models import Product, Order, OrderItem, OrderTicket, Customer
from .forms import OrderTicketForm


def get_lading_page(request):
    products = Product.objects.all()
    return render(request, 'store/lading.html', context={'products': products})


def get_company_page(request):
    return render(request, 'store/company.html')


def get_contact_us_page(request):
    return render(request, 'store/contact_us.html')


def get_product_page(request, product_name):
    product = Product.objects.get(name=product_name)
    context = {'product': product, 'lang': request.LANGUAGE_CODE}
    return render(request, 'store/product.html', context=context)


def get_products_page(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, placed=False)
        order_items = order.get_order_items
    else:
        order = {'get_order_items': 0, 'get_order_total': 0}
        order_items = order['get_order_items']

    tags = Tag.objects.all()
    products = Product.objects.all()
    context = {'products': products, 'order_items': order_items, 'tags': tags, 'lang': request.LANGUAGE_CODE}
    return render(request, 'store/products.html', context=context)


@login_required
@allowed_groups(['user'])
def get_order_page(request):
    return render(request, 'store/order.html')


@login_required
@allowed_groups(['user'])
def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    quantity = data['quantity']

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, placed=False)
    product = Product.objects.get(id=product_id)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    is_deleted = False

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
        order_item.save()
    elif action == 'down':
        order_item.quantity = (order_item.quantity - 1)
        order_item.save()
    elif action == 'set_quantity':
        order_item.quantity = int(quantity)
        order_item.save()
    elif action == 'remove':
        order_item.delete()
        is_deleted = True

    if order_item and order_item.quantity <= 0:
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
def remove_all_items_from_cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, placed=False)

    OrderItem.objects.filter(order=order).delete()

    context = {
        'quantity': 0,
        'total_quantity': 0,
        'get_order_total': 0,
        'product_total_price': 0,
        'delete_all': True
    }

    return JsonResponse(context)


@login_required
@allowed_groups(['user'])
def place_order(request):
    data = json.loads(request.body)
    order_code = data['order_code']

    if request.user.is_authenticated:
        order = Order.objects.get(order_code=order_code)
        if order.orderitem_set.count() > 0:
            order.placed = True
            order.save()
            return JsonResponse({'message': 'success'})
        else:
            return JsonResponse({'message': 'failed'})


@login_required
@allowed_groups(['user'])
def order_history(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer, placed=True).all()
    else:
        orders = {'get_order_items': 0, 'get_order_total': 0}

    context = {'orders': orders}
    return render(request, 'store/order_history.html', context=context)


@login_required
@allowed_groups(['user'])
def order_detail(request, order_code):

    order = Order.objects.get(order_code=order_code)
    ticket_message = order.orderticket_set.filter(type=2)
    ticket_status = order.orderticket_set.filter(type=1)
    form = OrderTicketForm(initial={'order': order_code})

    context = {
        'order': order,
        'tickets_message': ticket_message,
        'tickets_status': ticket_status,
        'form': form
    }

    if request.method == 'POST':
        form = OrderTicketForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            order = Order.objects.get(order_code=order_code)
            customer = request.user.customer

            print(order.order_code)
            ticket = OrderTicket(subject=subject, message=message, customer=customer, order=order)
            ticket.save()
            messages.success(request, 'Comment was saved !')
            return redirect('store:order_detail', order_code=order.order_code)
        else:
            messages.success(request, 'Error!')
            context['form'] = form
            return render(request, 'store/order_detail.html', context)
    else:
        return render(request, 'store/order_detail.html', context)


@login_required
@allowed_groups(['user'])
def get_products_by_tag(request, tag_name):
    products = Product.objects.filter(tags__name=tag_name)
    context = {'products': products}
    return render(request, 'store/products.html', context=context)

