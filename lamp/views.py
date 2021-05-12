from django.shortcuts import render
from django.http import HttpResponse, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *
from himiya.models import * 
from dvorniki.models import * 
from accessories.models import * 
from emergency.models import * 
from uhod.models import * 

from collections import defaultdict

import pandas as pd
import urllib.parse

# to serialize to json format
from django.core import serializers

# Create your views here.

def get_static_context():
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    accessories_categories = AccessoriesCategory.objects.all()
    emergency_categories = EmergencyCategory.objects.all()
    uhod_categories = UhodCategory.objects.all()
    static_context = {
        'categories': ct,
        'himiya_categories': himiya_categories,
        'accessories_categories': accessories_categories,
        'emergency_categories': emergency_categories,
        'uhod_categories': uhod_categories,
    }
    return static_context

static_context = get_static_context()

def about_us(request):
    template = 'lamp/about_us.html'
    context = {}
    context.update(static_context)
    return render(request, template, context)

def delivery(request):
    template = 'lamp/delivery.html'
    context = {}
    context.update(static_context)
    return render(request, template, context)

def contacts(request):
    template = 'lamp/contacts.html'
    context = {}
    context.update(static_context)
    return render(request, template, context)

def index(request):
    autos = Cars.objects.values('mark').distinct()
    
    brands = Brand.objects.all()

    # tests here
    marks = Cars.objects.values('mark', 'mark_norm').distinct()
    models = Cars.objects.values('model').distinct()
    gens = Cars.objects.values('gen').distinct()
    types = Type.objects.all()
    lamps = Lamps.objects.all()
    f_tags = lamps.values('f_tag').distinct()

    # lamps_json = serializers.serialize('json', lamps)
    context = {
        'cars': autos,
        'brands': brands,

        'lamps': lamps,
        'marks': marks,
        'models': models,
        'gens': gens,
        'types': types,
        'feature_tags': f_tags,
    }
    context.update(static_context)
    # tests endgs
    return render(request, 'lamp/index.html', context)

def mark(request, car_mark):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    car_mark = urllib.parse.unquote(car_mark)
    a = Cars.objects.values('mark', 'model').distinct()
    models = a.filter(mark = car_mark)


    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'models': models,
        'selected_mark': car_mark,
    }
    context.update(static_context)
    return render(request, 'lamp/mark.html', context)

def model(request, car_mark, car_model):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    car_mark = urllib.parse.unquote(car_mark)
    car_model = urllib.parse.unquote(car_model)
    generation = Cars.objects.filter(mark = car_mark, model = car_model)

    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'gen': generation,
        'selected_mark': car_mark,
        'selected_model': car_model,
    }
    context.update(static_context)
    return render(request, 'lamp/model.html', context)

def gen(request, car_mark, car_model, car_gen):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    car_mark = urllib.parse.unquote(car_mark)
    car_model = urllib.parse.unquote(car_model)
    car_gen = urllib.parse.unquote(car_gen)


    #    Ищем машину по марке, модели, поколению, получаем искомое авто
    auto = Cars.objects.filter(mark=car_mark, model=car_model, gen=car_gen)

    # Ссылаясь на искомое авто, получаем lamps_set для него
    lamps = auto[0].lamps_set.all()

    # берем колонку destination в лампах
    l_dest = lamps.values('destination')

    # Получаем те объекты Destination, id которых равно id из списка l_dest,
    # в котором мы оставили destination для нашего авто
    dest = Destination.objects.filter(id__in = l_dest)

    # берем колонку category в лампах
    l_cat = lamps.values('category')

    # Получаем те объекты Category, id которых равно id из списка l_cat,
    # в котором мы оставили category для нашего авто
    cat = Category.objects.filter(id__in = l_cat)

    # Из таблицы ламп оставляем колонки destination, category, вызываем метод
    # distinct(), чтобы убрать дубликаты
    lamps_new = lamps.values('destination', 'category',).distinct()

    # Создаем список, в который мы закидываем вместо idшников назначение и категории
    dest_cat = []
    for lamp in lamps_new:
        c_dest = dest.get(pk = lamp['destination']).dest
        c_cat = cat.get(pk = lamp['category']).cat
        dest_cat.append([c_dest, c_cat])

    # Оформляем список в массив, в котором destination - ключи, а
    # категории - значения. У каждого ключа создаем список значений, в который
    # мы добавляем значения
    dc = {key: [] for key, _ in dest_cat}
    for key, value in dest_cat:
        dc[key].append(value)

    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'selected_mark': car_mark,
        'selected_model': car_model,
        'selected_gen': car_gen,
        'destCat': dc,
    }
    context.update(static_context)
    return render(request, 'lamp/gen.html', context)

def car_lamps(request, car_mark, car_model, car_gen, dest, cat):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    car_mark = urllib.parse.unquote(car_mark)
    car_model = urllib.parse.unquote(car_model)
    car_gen = urllib.parse.unquote(car_gen)
    dest = urllib.parse.unquote(dest)
    cat = urllib.parse.unquote(cat)


    car = Cars.objects.filter(mark = car_mark, model = car_model, gen = car_gen)
    lamps = car[0].lamps_set.all()
    lamps = lamps.filter(destination__dest = dest, category__cat = cat)

    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'selected_mark': car_mark,
        'selected_model': car_model,
        'selected_gen': car_gen,
        'destination': dest,
        'category': cat,
        'lamps': lamps,
    }
    context.update(static_context)
    return render(request, 'lamp/car_lamps.html', context)

def product(request, product_name):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()

    product_name = urllib.parse.unquote(product_name)
    product = Lamps.objects.filter(name = product_name)
    pr_type = Lamps.objects.filter(ltype = product[0].ltype)
    cross_cars = pr_type[0].cars.all()
    cross_mark =  cross_cars.values('mark', 'mark_norm').distinct()
    print(len(cross_mark))

    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'product': product[0],
        'cross_cars': cross_cars,
        'cross_mark': cross_mark,
    }
    context.update(static_context)
    return render(request, 'lamp/product.html', context)

def category(request, cat):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    cat = urllib.parse.unquote(cat)
    category = Lamps.objects.filter(category__cat = cat)

    autos = Cars.objects.values('mark').distinct()
    brands = Brand.objects.all()
    # tests here
    marks = Cars.objects.values('mark', 'mark_norm').distinct()
    models = Cars.objects.values('model').distinct()
    gens = Cars.objects.values('gen').distinct()
    types = Type.objects.all()
    lamps = Lamps.objects.all()
    f_tags = lamps.values('f_tag').distinct()

    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'category': cat,
        'cars': autos,
        'brands': brands,
        'lamps': lamps,
        'marks': marks,
        'models': models,
        'gens': gens,
        'types': types,
        'feature_tags': f_tags,
    }
    context.update(static_context)
    return render(request, 'lamp/category.html', context)

def lamps_type(request, type, cat):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()

    type = urllib.parse.unquote(type)
    cat = urllib.parse.unquote(cat)

    lamps = Lamps.objects.filter(ltype__name = type, category__cat = cat)
    print(lamps)
    def get_lamp_type_cars(lamps):
        cars = lamps[0].cars.all()
        print(cars)
        marks = cars.values('mark')

        data = pd.DataFrame(marks)
        # data = pd.DataFrame.from_dict(marks)

        # data = data.pivot_table(index=['mark'], aggfunc = 'size')
        # mcount = data.to_frame(name = 'counts')
        # mcount = mcount.sort_values(by='counts')

        mcount = data.groupby(data.columns.tolist(),as_index=True).size()
        mcount = mcount.to_frame(name = 'counts')
        mcount = mcount.sort_values(by = 'counts', ascending=False)

        marks = list(mcount.index[:10])
        marks_count = list(mcount['counts'][:10])
        return marks, marks_count

    marks, marks_count = get_lamp_type_cars(lamps)

    marks_length = len(marks_count)

    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'lamps': lamps,
        'marks': marks,
        'marks_count': marks_count,
        'marks_length': marks_length,
    }
    context.update(static_context)
    return render(request, 'lamp/type.html', context)

def brand(request, brand, cat):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()

    brand = urllib.parse.unquote(brand)
    cat = urllib.parse.unquote(cat)

    lamps = Lamps.objects.filter(brand__name = brand, category__cat = cat)

    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'selected_brand': brand,
        'selected_category': cat,
        'lamps': lamps,
    }
    context.update(static_context)
    return render(request, 'lamp/brand.html', context)

def allbrands(request):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    brands = Brand.objects.all()

    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'brands': brands,
    }
    context.update(static_context)
    return render(request, 'lamp/allbrands.html', context)

def spesbrand(request, brand):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()
    brand = urllib.parse.unquote(brand)

    brand = Brand.objects.get(name = brand)
    brand_lamps = Lamps.objects.filter(brand = brand)

    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'brand': brand,
        'lamps': brand_lamps,
    }
    context.update(static_context)
    return render(request, 'lamp/spesbrand.html', context)

def search(request):
    ct = Category.objects.all()
    himiya_categories = HimiyaCategory.objects.all()

    s = request.GET['q']

    lamps = Lamps.objects.filter(name__contains = s)

    if (len(lamps) == 0):
        message = 'no lamps found'
    
    context = {
        'himiya_categories': himiya_categories,
        'categories': ct,
        'lamps': lamps,
    }
    context.update(static_context)
    return render(request, 'lamp/search.html', context)

def form_car(request):

    if request.GET.get('mark')  and  not request.GET.get('model'):
        mark = request.GET.get('mark')
        mark = urllib.parse.unquote(mark)
        return HttpResponseRedirect(reverse('lamp:mark', args = [mark]))
    elif request.GET.get('model') and not request.GET.get('gen'):
        mark = request.GET.get('mark')
        mark = urllib.parse.unquote(mark)
        model = request.GET.get('model')
        model = urllib.parse.unquote(model)
        if model == 'Выберите модель':
            return HttpResponseRedirect(reverse('lamp:mark', args = [mark]))
        return HttpResponseRedirect(reverse('lamp:model', args = [mark, model]))
    else:
        mark = request.GET.get('mark')
        mark = urllib.parse.unquote(mark)
        model = request.GET.get('model')
        model = urllib.parse.unquote(model)
        gen = request.GET.get('gen')
        gen = urllib.parse.unquote(gen)
        if gen == 'Выберите поколение':
            return HttpResponseRedirect(reverse('lamp:model', args = [mark, model]))
        return HttpResponseRedirect(reverse('lamp:gen', args = [mark, model, gen]))

def form_car_ajax(request):

    if (request.is_ajax and request.GET.get('mark', None)):
        mark = request.GET['mark']
        mark = urllib.parse.unquote(mark)

        models = Cars.objects.filter(mark = mark).values('model').distinct()

        return JsonResponse({'models': list(models) }, status = 200)
    elif (request.is_ajax and request.GET.get('model', None)):
        model = request.GET['model']
        model = urllib.parse.unquote(model)

        gens = Cars.objects.filter(model = model).values('gen')

        return JsonResponse({'gens': list(gens) }, status = 200)

    mark = request.GET['mark']
    mark = urllib.parse.unquote(mark)

    return HttpResponseRedirect(reverse('lamp:mark', args = [mark]))



# JSON
def filter_update_lamps(request):
    # print(request)

    l2 = Lamps.objects.all()


    ftype = request.GET['filter_type']
    fbrand = request.GET['filter_brand']
    ftags = request.GET['filter_tags']

    if ftype:
        ftype = ftype.split(',')
        l2 = l2.filter(ltype__name__in = ftype)
    if fbrand:
        fbrand = fbrand.split(',')
        fbrand = [urllib.parse.unquote(item) for item in fbrand]
        l2 = l2.filter(brand__name__in = fbrand)
    if ftags:
        ftags = ftags.split(',')
        ftags = [urllib.parse.unquote(item) for item in ftags]
        ftags = [item.replace("_", " ") for item in ftags]

        print(ftags)
        l2 = l2.filter(f_tag__in = ftags)

    return render(request, 'lamp/blocks/products_list.html', {
        'lamps': l2,
    })


