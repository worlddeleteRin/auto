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

static_context = get_static_context()


def index(request):
# ct = Category.objects.all()
    ct = Category.objects.all()
    accessories_categories = AccessoriesCategory.objects.all()
    accessories_products = AccessoriesItem.objects.all()
    template = 'accessories/index.html'
    context = {
        'accessories_categories': accessories_categories,
        'categories': ct,
        'accessories_products': accessories_products,
    }
    context.update(static_context)
    return render(request, template, context)

def product(request, product_id):
    ct = Category.objects.all()
    accessories_categories = AccessoriesCategory.objects.all()
    current_product = AccessoriesItem.objects.get(
        id = product_id
    )
    template = 'accessories/product.html'
    context = {
        'accessories_categories': accessories_categories,
        'categories': ct,
        'product': current_product,
    }
    context.update(static_context)
    return render(request, template, context)

def category(request, category_id):
    ct = Category.objects.all()
    accessories_categories = AccessoriesCategory.objects.all()
    current_category = AccessoriesCategory.objects.get(
        id = category_id
    )
    accessories_products = current_category.accessoriesitem_set.all()
    template = 'accessories/category.html'
    context = {
        'accessories_categories': accessories_categories,
        'categories': ct,
        'current_category': current_category,
        'accessories_products': accessories_products,
    }
    context.update(static_context)
    return render(request, template, context)

