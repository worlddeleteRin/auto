#!/usr/bin/env python3

from dvorniki.models import *
import pandas as pd
import numpy as np
import os
import pandas as pd
import requests
import base64
import math

path = '/Users/noname/learn/django/auto_scrape/dvorniki/'

def createcars():
    i = 0
    found = 0
    print('----------------------')
    print('start creating cars')
    print('----------------------')
    data = pd.read_csv(path + 'cars_main.csv')
    for index, item in data.iterrows():
        mark = item['mark']
        model = item['model']
        gen = item['gen']
        gen_imgurl = item['gen_imgurl']
        items = item['items']

        current_mark = Dvmark.objects.get_or_create(
            name = mark,
        )[0]
        current_model = Dvmodel.objects.get_or_create(
            mark = current_mark,
            name = model,
        )[0]

        current_gen = Dvgen.objects.get_or_create(
            model = current_model,
            name = gen,
        )[0]

        new_car = Dvcar.objects.get_or_create(
            mark = current_mark,
            model = current_model,
            gen = current_gen,
            gen_img = gen_imgurl,
        )[0]
        i = i + 1
        print('processed', i, 'cars')
        for p in eval(items):
            if (Dvornik.objects.filter(name=p).exists()):
                found = found + 1
                print('found with products', found, 'cars')
                dv = Dvornik.objects.filter(name = p)
                for dvornik in dv:
                    dvornik.cars.add(new_car)
    


def createdvorniki():
    i = 0
    data = pd.read_csv(path + 'data2.csv')

    for index, item in data.iterrows():
        print('start creating new product')

        brand_name = item['brand_name']
        print('brand name is', brand_name)
        brand = Dvbrand.objects.get_or_create(
            name = brand_name,
        )[0]
        print('brand is', brand)
        series_name = item['series_name']
        print('series name is', series_name)
        series = Dvser.objects.get_or_create(
            name = str(series_name)
        )[0]
        print('series is', series)

        tip_dvornika = item['tip_dvornika']
        print('dvornik type is', tip_dvornika)
        dvtype = Dvtype.objects.get_or_create(
            name = str(tip_dvornika)
        )[0]
        print('dv type is', dvtype)

        name = item['item_name']
        price = item['price']
        imgsrc = item['imgurl']
        if math.isnan(price):
            price = 0
        new_dvornik = Dvornik(
            brand = brand,
            ser = series,
            dvtype = dvtype,
            name = str(name),
            price = int(price),
            imgsrc = imgsrc,
        )
        new_dvornik.save()

        print('Добавление креплений')
        for kr in eval(item['kreplenie']):
            new_kr = Dvkreplenie.objects.get_or_create(
                name = kr
            )[0]
            new_dvornik.kreplenie.add(new_kr)

        i = i + 1
        print('created', i)
    print('created all', i)



def createall():
    createdvorniki()
    createcars()

if __name__ == "__main__":
    createall()


