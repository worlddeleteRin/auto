#!/usr/bin/env python3
from himiya.models import * 
import pandas as pd
import requests

IMAGE_PATH = '/Users/noname/learn/django/auto/static/images/himiya/'
PRODUCTS_PATH = '/Users/noname/learn/django/auto/scrape/himiya.csv'


def createall():
    i = 0
    print('start creating products')
    data = pd.read_csv(PRODUCTS_PATH)
    for index, item in data.iterrows():
        sku = item['sku']
        name = item['name']
        imgurl = item['imgurl']
        category = item['category']
        description = item['description']
        # download image
        img = requests.get(imgurl).content
        # save image
        image_name = 'himiya_product_' + str(index)+'.png'
        file = open(IMAGE_PATH + image_name, 'wb')
        file.write(img)
        file.close()
        imgurl = 'static/images/himiya' + image_name

        cat = HimiyaCategory.objects.get_or_create(
            name = category
        )[0]
        new_product = HimiyaItem(
            category = cat,
            sku = sku,
            name = name,
            description = description,
            imgurl = image_name,
        )
        new_product.save()
        i += 1
        print('create', i, 'products')


if __name__ == "__main__":
    createall()






