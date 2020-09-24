from django.db import models

# Create your models here.

class Cart(models.Model):  
    created_at = models.DateTimeField(auto_now_add = True) 
    session_key = models.CharField(max_length = 200)

    def get_total(self):
        total = 0
        for item in self.item_set.all():
            total += item.price * item.quantity
        return total


class Orders(models.Model):

    name = models.CharField(max_length = 200, default = '')
    phone = models.CharField(max_length = 50, default = '')
    email = models.CharField(max_length = 200, default = '')


class Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, default = None,
    blank = True, null = True)
    order = models.ForeignKey(Orders, on_delete = models.DO_NOTHING, 
    default = None, blank = True, null = True)

    name = models.CharField(max_length = 200, default = '')
    price = models.IntegerField(default = 0)
    quantity = models.IntegerField(default = 1)

    def product_order_price(self):
        return self.price * self.quantity

    def __str__(self):
        return self.name 
    









def delete_all_cart():
    carts = Cart.objects.all()
    items = Item.objects.all()
    orders = Orders.objects.all()
    carts.delete()
    print("All carts are deleted")
    items.delete()
    print("All items are deleted")
    orders.delete()
    print("All orders are deleted")





