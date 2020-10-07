from django.db import models

# Create your models here.


class Dvmark(models.Model):
    name = models.CharField(max_length=100, default = '')
    def __str__(self):
        return self.name

class Dvmodel(models.Model):
    mark = models.ForeignKey(Dvmark, on_delete = models.DO_NOTHING,)
    name = models.CharField(max_length=200, default = '')
    def __str__(self):
        return self.name

class Dvgen(models.Model):
    mark = models.ForeignKey(Dvmark, on_delete = models.DO_NOTHING,)
    model = models.ForeignKey(Dvmodel, on_delete = models.DO_NOTHING,)
    name = models.CharField(max_length=200, default = '')

class Dvcar(models.Model): 
    mark = models.ForeignKey(Dvmark, on_delete = models.DO_NOTHING,)
    model = models.ForeignKey(Dvmodel, on_delete = models.DO_NOTHING,)
    gen = models.ForeignKey(Dvgen, on_delete = models.DO_NOTHING,)      


    gen_img = models.CharField(max_length = 3000,
    default="https://placehold.it/420x327")

    def __str__(self):
        return self.mark.name + ' ' + self.model.name + ' ' + self.gen

    
class Dvkreplenie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dvtype(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Dvbrand(models.Model):
    name = models.CharField(max_length = 200)
    # image = models.CharField(max_length = 3000, default = 'https://placehold.it/50x50')
    # description = models.CharField(max_length = 3000, default = '')

    def __str__(self):
        return self.name


class Dvser(models.Model):
    name = models.CharField(max_length = 200)
    # image = models.CharField(max_length = 3000, default = 'https://placehold.it/50x50')
    # description = models.CharField(max_length = 3000, default = '')

    def __str__(self):
        return self.name
    
    
class Dvornik(models.Model):

    cars = models.ManyToManyField(Dvcar) 
    kreplenie = models.ManyToManyField(Dvkreplenie)

    brand = models.ForeignKey(Dvbrand, on_delete = models.DO_NOTHING)
    ser = models.ForeignKey(Dvser, on_delete = models.DO_NOTHING,)
    dvtype = models.ForeignKey(Dvtype, on_delete = models.DO_NOTHING,)
     

    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    imgsrc = models.CharField(max_length = 2000, default="https://placehold.it/420x327")
    
    
    def __str__(self):
        return self.name

    
def dvdeleteall():
    dvmark = Dvmark.objects.all()
    dvmodel = Dvmodel.objects.all()
    dv = Dvornik.objects.all()
    dvt = Dvtype.objects.all()
    dvser = Dvser.objects.all()
    dvb = Dvbrand.objects.all()
    dvkr = Dvkreplenie.objects.all()
    dvcar = Dvcar.objects.all()

    
    dvkr.delete()
    dv.delete()
    dvt.delete()
    dvser.delete()
    dvb.delete()
    dvcar.delete()
    dvmodel.delete()
    dvmark.delete()
    
    
    print('All cars deleted')
    





