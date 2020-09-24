import os 
import pandas as pd
from lamp.models import * 

main_path = os.getcwd()

def createlamps():
    print('---------------------')
    print('start creating lamps')
    print('---------------------')
    data = pd.read_csv(main_path + '/data_main/all_lamps.csv')
    i = 0
    for index, row in data.iterrows(): 
        new_lamp = Lamps(
            brand = Brand.objects.get_or_create(name=row.brand)[0],
            ltype = Type.objects.get_or_create(name=row.lamp_type)[0],
            destination = Destination.objects.get_or_create(dest = 'Нет назначения')[0],
            category = Category.objects.get_or_create(cat = row.category)[0],
            name = row.product_name,
            price = row.price,
            socle = 'nosocle',
            feature = row.features,
            f_tag = row['f_tag'],
            imgsrc = row['image'],
            )
        new_lamp.save()
        print(new_lamp.name, 'lamp created')
        i = i + 1
    print('Created', i, 'lamps')
    print('---------------------')
    print('end creating lamps')
    print('---------------------')


def createcars():
    print('---------------------')
    print('start creating cars')
    print('---------------------')
    autofile = pd.read_csv(main_path + '/data_main/cars.csv')
    not_exist = 0
    i = 1
    for index, item in autofile.iterrows(): 
        car = Cars.objects.get_or_create(
            mark = item['auto_mark'],
            mark_norm = item['auto_mark_norm'],
            model = item['model_link'],
            gen = item['gen_link'],
            gen_img = item['gen_img-src']
        )
        if (Lamps.objects.filter(name = item['product_link']).exists()):
            lamp = Lamps.objects.filter(
                name = item['product_link'],
            )[0]
            lamp.destination = Destination.objects.get_or_create(
                dest = item['destination']
            )[0]
            lamp.save()
            car[0].lamps_set.add(lamp)
            print("Created ", i, " relations")
            print("Car: ", car[0].mark, " ", car[0].model, car[0].gen)
            print("Lamp:", lamp.name)
            i = i + 1
        else:
            print('lamp', item['product_link'], 'not exist') 
            not_exist = not_exist + 1
            print(item['product_link'] ,'not exist')
    print('crated', i)
    print('not exist', not_exist)
    print('---------------------')
    print('end creating lamps')
    print('---------------------')



def createbrands():
    print('---------------------')
    print('start creating brands')
    print('---------------------')
    brands = pd.read_csv('/Users/noname/work/lamp/brands/allbrands.csv')
    i = 1
    for index, row in brands.iterrows():
        new_brand = Brand(
            name = row['brand_name'],
            image = row['brand_img-src'],
            description = row['description'],
        )
        new_brand.save()
        print('Created brand:', new_brand.name)
        i = i + 1
    print('Created', i, 'brands')
    print('---------------------')
    print('end creating lamps')
    print('---------------------')

def createall():
    createbrands()
    createlamps()
    createcars()

if __name__ == "__main__":
    createall()

    
            
            

        
