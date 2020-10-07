from django.db import models

# Create your models here.

class Cars(models.Model): 
    mark = models.CharField(max_length=100)
    mark_norm = models.CharField(max_length = 100, default='-')
    model = models.CharField(max_length=100)
    gen = models.CharField(max_length=100)

    gen_img = models.CharField(max_length = 3000,
    default="https://placehold.it/420x327")

    def __str__(self):
        return self.mark + ' ' + self.model + ' ' + self.gen

    
class Destination(models.Model):
    dest = models.CharField(max_length=100)

    def __str__(self):
        return self.dest

class Category(models.Model):
    cat = models.CharField(max_length=100)

    def __str__(self):
        return self.cat

class Type(models.Model):
    name = models.CharField(max_length = 100)  

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length = 200)
    image = models.CharField(max_length = 3000, default = 'https://placehold.it/50x50')
    description = models.CharField(max_length = 3000, default = '')

    def __str__(self):
        return self.name
    
    


class Lamps(models.Model):

    cars = models.ManyToManyField(Cars) 
    brand = models.ForeignKey(Brand, on_delete = models.DO_NOTHING)
    ltype = models.ForeignKey(Type, on_delete = models.DO_NOTHING,)
    destination = models.ForeignKey(Destination, on_delete = models.DO_NOTHING,)
    category = models.ForeignKey(Category, on_delete = models.DO_NOTHING)

    name = models.CharField( max_length=300)
    price = models.IntegerField(default=0)
    socle = models.CharField(max_length = 50, default='-')
    feature = models.CharField(max_length = 100, default='-')
    f_tag = models.CharField(max_length = 100, default='-')
    feature_desc = models.CharField(max_length = 3000, default = '')
    attributes = models.CharField(max_length = 3000, default = '')
    description = models.CharField(max_length = 3000, default = '')

    imgsrc = models.CharField(max_length = 2000, default="https://placehold.it/420x327")
    
    
    def __str__(self):
        return self.name

    
def lampdeleteall():
    lamp = Lamps.objects.all()
    types = Type.objects.all()
    cat = Category.objects.all()
    dest = Destination.objects.all()
    brand = Brand.objects.all()
    cars = Cars.objects.all()

    lamp.delete()
    print('All lamps deleted')
    types.delete()
    print('All types deleted')
    cat.delete()
    print('All categories deleted')
    dest.delete()
    print('All destinations deleted')
    brand.delete()
    print('All brands deleted')
    cars.delete()
    print('All cars deleted')
    





