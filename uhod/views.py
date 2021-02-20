from django.shortcuts import render
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *
from lamp.models import * 
from lamp.views import get_static_context


from collections import defaultdict

import pandas as pd
import urllib.parse

main_category = 'uhod'

static_context = get_static_context()

def index(request):
# ct = Category.objects.all()
    ct = Category.objects.all()
    uhod_categories = UhodCategory.objects.all()
    uhod_products = UhodItem.objects.all()
    template = 'uhod/index.html'
    context = {
        'uhod_categories': uhod_categories,
        'categories': ct,
        'uhod_products': uhod_products,
        'main_category': main_category
    }
    context.update(static_context)
    return render(request, template, context)

def product(request, product_id):
    ct = Category.objects.all()
    uhod_categories = UhodCategory.objects.all()
    current_product = UhodItem.objects.get(
        id = product_id
    )
    template = 'uhod/product.html'
    context = {
        'uhod_categories': uhod_categories,
        'categories': ct,
        'product': current_product,
    }
    context.update(static_context)
    return render(request, template, context)

def category(request, category_id):
    ct = Category.objects.all()
    uhod_categories = UhodCategory.objects.all()
    current_category = UhodCategory.objects.get(
        id = category_id
    )
    uhod_products = current_category.uhoditem_set.all()
    template = 'uhod/category.html'
    context = {
        'uhod_categories': uhod_categories,
        'categories': ct,
        'current_category': current_category,
        'uhod_products': uhod_products,
    }
    context.update(static_context)
    return render(request, template, context)

