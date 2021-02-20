from django.db import models

# Create your models here.


class UhodCategory(models.Model):
    name = models.CharField(max_length = 300, default = None)
    def __str__(self):
        return self.name

class UhodItem(models.Model):
    category = models.ForeignKey(UhodCategory, on_delete=models.CASCADE,
     blank = True, null = True)
    sku = models.CharField(max_length = 100, default = None)
    name = models.CharField(max_length = 300, default = None)
    price = models.IntegerField(default = None, 
    blank = True, null = True)
    description = models.TextField(default = None)
    imgurl = models.ImageField(upload_to = 'static/images/uhod')
    def __str__(self):
        return str(self.id) + self.name

def delalluhod():
    c = UhodCategory.objects.all()
    i = UhodItem.objects.all()
    c.delete()
    i.delete()
    print('all uhod deleted')



