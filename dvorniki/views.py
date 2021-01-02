from django.shortcuts import render
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *
from lamp.models import * 

from collections import defaultdict

import pandas as pd
import urllib.parse


def index(request):
    ct = Category.objects.all()
    
    marks = Dvmark.objects.all()

    dv_brands = Dvbrand.objects.all()

    return render(request, 'dvorniki/index.html', {
        'categories': ct,

        'marks': marks,
        'dvbrands': dv_brands,
    })


def mark(request, mark_id):
    ct = Category.objects.all()
    
    current_mark = Dvmark.objects.get(
        id = mark_id
    )
    models = Dvmodel.objects.filter(
        mark = current_mark,
    )
    

    return render(request, 'dvorniki/mark.html', {
        'categories': ct,

        'selected_mark': current_mark,
        'models': models,
    })

def model(request, mark_id, model_id):
    ct = Category.objects.all()
    
    current_mark = Dvmark.objects.get(
        id = mark_id
    )
    current_model = Dvmodel.objects.get(
        id = model_id
    )

    cars = Dvcar.objects.filter(
        mark = current_mark,
        model = current_model,
    )
    
    return render(request, 'dvorniki/model.html', {
        'categories': ct,

        'selected_mark': current_mark.name,
        'selected_model': current_model.name,
        'cars': cars,
    })

def gen(request, mark_id, model_id, gen_id):
    ct = Category.objects.all()
    
    current_mark = Dvmark.objects.get(
        id = mark_id
    )
    current_model = Dvmodel.objects.get(
        id = model_id
    )
    current_gen = Dvgen.objects.get(
        id = gen_id 
    )

    cars = Dvcar.objects.filter(
        mark = current_mark,
        model = current_model,
        gen = current_gen,
    )
    print('here is first cars')
    print(cars)
    cars = list(cars.values_list('id', flat=True))
    print('here is cars')
    print(cars)
    dvorniki = Dvornik.objects.filter(
        cars__in = cars,
    )

    print('here is dvorniki')
    print(dvorniki)
    
    return render(request, 'dvorniki/gen.html', {
        'categories': ct,

        'selected_mark': current_mark.name,
        'selected_model': current_model.name,
        'selected_gen': current_gen.name,
        # 'cars': cars,
        'dvorniki': dvorniki,
    })

def product(r, product_id):
    ct = Category.objects.all()

    product = Dvornik.objects.get(
        id = product_id,
    )

    cross_m = product.cars.all().values('mark').distinct()
    cross_marks = Dvmark.objects.filter(
        id__in = cross_m,
    )
    cross_cars = product.cars.all()

    return render(r, 'dvorniki/product.html', {
         'categories': ct,

         'product': product,
         'cross_marks': cross_marks,
         'cross_cars': cross_cars,
    })


def series(r, ser_id):
    ct = Category.objects.all()

    current_ser = Dvser.objects.get(
        id = ser_id
    )
    dvorniki = Dvornik.objects.filter(
        ser = current_ser,
    )

    return render(r, 'dvorniki/series.html', {
         'categories': ct,

         'current_ser': current_ser,
         'dvorniki': dvorniki,
    })

