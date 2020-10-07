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

    return render(request, 'dvorniki/index.html', {
        'categories': ct,

        'marks': marks,
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
    cars = cars.values('id')

    dvorniki = Dvornik.objects.filter(
        cars__in = [cars]
    )
    
    return render(request, 'dvorniki/gen.html', {
        'categories': ct,

        'selected_mark': current_mark.name,
        'selected_model': current_model.name,
        'selected_gen': current_gen.name,
        # 'cars': cars,
        'dvorniki': dvorniki,
    })


