from django.db import models

# Create your models here.


class AccessoriesCategory(models.Model):
    name = models.CharField(max_length = 300, default = None)
    def __str__(self):
        return self.name

class AccessoriesItem(models.Model):
    category = models.ForeignKey(AccessoriesCategory, on_delete=models.CASCADE,
     blank = True, null = True)
    sku = models.CharField(max_length = 100, default = None)
    name = models.CharField(max_length = 300, default = None)
    price = models.IntegerField(default = None, 
    blank = True, null = True)
    description = models.TextField(default = None)
    imgurl = models.ImageField(upload_to = 'static/images/accessories')
    def __str__(self):
        return str(self.id) + self.name

def delallaccessories():
    c = AccessoriesCategory.objects.all()
    i = AccessoriesItem.objects.all()
    c.delete()
    i.delete()
    print('all accessories deleted')



