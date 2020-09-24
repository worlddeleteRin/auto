from django.contrib import admin

from .models import *

class ItemInline(admin.TabularInline):
    model = Item

class OrdersAdmin(admin.ModelAdmin):
  fieldsets = [
      ('Покупатель', {'fields': ['name', 'phone', 'email']}),
  ]  
  inlines = [ItemInline]



admin.site.register(Cart)
admin.site.register(Item)
admin.site.register(Orders, OrdersAdmin)
