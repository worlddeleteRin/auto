from django.db import models

# Create your models here.


class HimiyaCategory(models.Model):
    name = models.CharField(max_length = 300, default = None)
    def __str__(self):
        return self.name

class HimiyaItem(models.Model):
    category = models.ForeignKey(HimiyaCategory, on_delete=models.DO_NOTHING, )
    sku = models.CharField(max_length = 100, default = None)
    name = models.CharField(max_length = 300, default = None)
    price = models.IntegerField(default = 0)
    description = models.TextField(default = None)
    imgurl = models.ImageField(upload_to = 'static/images/himiya')
    def __str__(self):
        return str(self.id) + self.name


