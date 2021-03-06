from django.db import models

# Create your models here.


class HimiyaCategory(models.Model):
    name = models.CharField(max_length = 300, default = None)
    def __str__(self):
        return self.name

class HimiyaItem(models.Model):
    category = models.ForeignKey(HimiyaCategory, on_delete=models.CASCADE,
     blank = True, null = True)
    sku = models.CharField(max_length = 100, default = None)
    name = models.CharField(max_length = 300, default = None)
    price = models.IntegerField(default = None, 
    blank = True, null = True)
    description = models.TextField(default = None)
    imgurl = models.ImageField(upload_to = 'static/images/himiya')
    def __str__(self):
        return str(self.id) + self.name

def delallhimiya():
    c = HimiyaCategory.objects.all()
    i = HimiyaItem.objects.all()
    c.delete()
    i.delete()
    print('all himiya deleted')



