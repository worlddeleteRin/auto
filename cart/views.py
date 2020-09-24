from django.shortcuts import render
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import * 

from lamp.models import *

import urllib.parse




def index(request):
    ct = Category.objects.all()
    if not request.session.session_key:
        request.session.create()
        current_session_key = request.session.session_key
    else:
        current_session_key = request.session.session_key
    
    cart = Cart.objects.get_or_create(
        session_key = current_session_key
    )

    cart_items = cart[0].item_set.all()


    return render(request, 'cart/index.html', {
        'session_key': current_session_key,
        'cart': cart[0],
        'cart_items': cart_items,
        'categories': ct,
    })

def add_product(request, product_name, product_price):

    product_name = urllib.parse.unquote(product_name)
    if not request.session.session_key:
        request.session.create()
        current_session_key = request.session.session_key
    else:
        current_session_key = request.session.session_key

    cart = Cart.objects.get_or_create(
        session_key = current_session_key
    )
    if (Item.objects.filter(cart__session_key = request.session.session_key,
    name = product_name).exists()):
        item = Item.objects.get(cart__session_key = request.session.session_key,
    name = product_name)
        item.quantity += 1
        item.save()
        return HttpResponseRedirect(reverse('cart:index'))
        # return HttpResponseRedirect(reverse(request.path_info))
    else:
        pr_item = Item(
            cart = cart[0],
            name = product_name,
            price = product_price,
        )
        pr_item.save()
        return HttpResponseRedirect(reverse('cart:index'))
        # return HttpResponseRedirect(request.path_info)

def remove_product(request, product_name):
    product_name = urllib.parse.unquote(product_name)
    # cart = Cart.objects.get_or_create(
    #     session_key = request.session.session_key
    # )
    pr_item = Item.objects.get(cart__session_key = request.session.session_key, name = product_name)
    pr_item.delete()

    return HttpResponseRedirect(reverse('cart:index'))

def remove_quantity(request, product_name):
    product_name = urllib.parse.unquote(product_name)
    pr_item = Item.objects.get(cart__session_key = request.session.session_key, name = product_name)
    pr_item.quantity -= 1
    if pr_item.quantity == 0:
        pr_item.delete()
        return HttpResponseRedirect(reverse('cart:index'))
    else:
        pr_item.save()
        return HttpResponseRedirect(reverse('cart:index'))

def create_order(request):
    name = request.POST['name']
    name = urllib.parse.unquote(name)
    phone = request.POST['phone']
    phone = urllib.parse.unquote(phone)
    email = request.POST['email']
    email = urllib.parse.unquote(email)

    cart = Cart.objects.get_or_create(
        session_key = request.session.session_key
    )[0]

    cart_items = cart.item_set.all()

    new_order = Orders(
        name = name,
        phone = phone,
        email = email,
    )
    new_order.save()

    for item in cart_items:
        new_order.item_set.add(item)
    
    return HttpResponseRedirect(reverse('cart:index'))


def add_product_ajax(request):
    if not request.session.session_key:
        request.session.create()
        current_session_key = request.session.session_key
    else:
        current_session_key = request.session.session_key

    cart = Cart.objects.get_or_create(
        session_key = current_session_key
    )[0]

    pr = Lamps.objects.get(id = request.GET['product_id'])
    product_name = pr.name
    product_price = pr.price

    if (Item.objects.filter(cart__session_key = current_session_key,
    name = product_name).exists()):
        item = Item.objects.get(cart__session_key = current_session_key,
    name = product_name)
        item.quantity += 1
        item.save()
        return JsonResponse({
            'created': 'yes',
            'is_new': 'no'
        }, status = 200)
        # return HttpResponseRedirect(reverse(request.path_info))
    else:
        pr_item = Item(
            cart = cart,
            name = product_name,
            price = product_price,
        )
        pr_item.save()
        return JsonResponse({
            'created': 'yes',
            'is_new': 'yes'
        }, status = 200)
        # return HttpResponseRedirect(request.path_info)

def remove_product_ajax(request):
    current_session_key = request.session.session_key
    cart = Cart.objects.get_or_create(
        session_key = current_session_key
    )[0]
    
    current_item = Item.objects.get(cart = cart, id = request.GET['pr_id'])
    
    current_item.delete()

    return JsonResponse({
        'removed': 'yes'
    },status = 200)

def remove_quantity_ajax(request):
    current_session_key = request.session.session_key
    cart = Cart.objects.get_or_create(
        session_key = current_session_key
    )[0]

    message  = ''
    print(request.GET['pr_id'])
    current_item = Item.objects.get(cart = cart, id = request.GET['pr_id'])
    if current_item.quantity == 1:
        current_item.delete()
        message = 'deleted'
        return JsonResponse({
            'message': message,
        }, status = 200)
    else:
        current_item.quantity -= 1
        current_item.save()
        message = current_item.quantity
        return JsonResponse({
            'message': message,
        },  status = 200)

def add_quantity_ajax(request):
    current_session_key = request.session.session_key
    cart = Cart.objects.get(session_key = current_session_key)
    pr_id = request.GET['pr_id']
    cr_item = Item.objects.get(
        cart = cart,
        id = pr_id
    )
    cr_item.quantity += 1
    cr_item.save()
    return JsonResponse({
        'quantity': cr_item.quantity,
    }, status = 200)

def update_sum_ajax(request):
    current_session_key = request.session.session_key
    cart = Cart.objects.get(session_key = current_session_key)

    item = Item.objects.get(
        cart = cart,
        id = request.GET['pr_id']
    )
    item_sum = item.quantity * item.price
    return JsonResponse({
        'sum': item_sum,
    }, status = 200)

def update_cartsum_ajax(request):
    current_session_key = request.session.session_key
    cart = Cart.objects.get(session_key = current_session_key)
    cart_summ = cart.get_total()

    return JsonResponse({

        'cart_summ': cart_summ,
    }, status = 200)

def create_order_ajax(request):
    current_session_key = request.session.session_key
    cart = Cart.objects.get(session_key = current_session_key)
    name = request.GET['name']
    phone = request.GET['phone']
    email = request.GET['email']
    
    order = Orders(
        name = name,
        phone = phone,
        email = email,
    )
    order.save()
    current_items = cart.item_set.all()

    for item in current_items:
        order.item_set.add(item)
    
    for item in cart.item_set.all():
        cart.item_set.remove(item)

    return JsonResponse({
        'created': 'yes'
    }, status = 200)
