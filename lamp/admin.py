from django.contrib import admin

from .models import Cars, Lamps, Category, Destination, Type, Brand

# Register your models here.


admin.site.register(Cars)
admin.site.register(Lamps)
admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(Type)
admin.site.register(Brand)