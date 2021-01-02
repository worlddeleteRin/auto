from django.urls import path 
from . import views
    
app_name = 'himiya'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('product/<int:product_id>', views.product, name = 'product'),
    path('category/<int:category_id>', views.category, name = 'category'),
]