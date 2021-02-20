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
    emergency_categories = EmergencyCategory.objects.all()
    emergency_products = EmergencyItem.objects.all()
    template = 'emergency/index.html'
    context = {
        'emergency_categories': emergency_categories,
        'categories': ct,
        'emergency_products': emergency_products,
    }
    context.update(static_context)
    return render(request, template, context)

def product(request, product_id):
    ct = Category.objects.all()
    emergency_categories = EmergencyCategory.objects.all()
    current_product = EmergencyItem.objects.get(
        id = product_id
    )
    template = 'emergency/product.html'
    context = {
        'emergency_categories': emergency_categories,
        'categories': ct,
        'product': current_product,
    }
    context.update(static_context)
    return render(request, template, context)

def category(request, category_id):
    ct = Category.objects.all()
    emergency_categories = EmergencyCategory.objects.all()
    current_category = EmergencyCategory.objects.get(
        id = category_id
    )
    emergency_products = current_category.emergencyitem_set.all()
    template = 'emergency/category.html'
    context = {
        'emergency_categories': emergency_categories,
        'categories': ct,
        'current_category': current_category,
        'emergency_products': emergency_products,
    }
    context.update(static_context)
    return render(request, template, context)

