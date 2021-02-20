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
    himiya_categories = HimiyaCategory.objects.all()
    himiya_products = HimiyaItem.objects.all()
    template = 'himiya/index.html'
    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'himiya_products': himiya_products,
    }
    context.update(static_context)
    return render(request, template, context)

def product(request, product_id):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    current_product = HimiyaItem.objects.get(
        id = product_id
    )
    template = 'himiya/product.html'
    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'product': current_product,
    }
    context.update(static_context)
    return render(request, template, context)


def category(request, category_id):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    current_category = HimiyaCategory.objects.get(
        id = category_id
    )
    himiya_products = current_category.himiyaitem_set.all()
    template = 'himiya/category.html'
    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'himiya_products': himiya_products,
    }
    context.update(static_context)
    return render(request, template, context)

