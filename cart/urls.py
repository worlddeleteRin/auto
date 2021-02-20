from django.urls import path 
from . import views

app_name = 'cart'

urlpatterns = [
    # ex: cart/
    path('', views.index, name = 'index'),
    # ex: add_product/some_name/some_price
    path('add_product/<str:product_name>/<int:product_price>', views.add_product, name = 'add_product'),
    path('add_product_ajax/', views.add_product_ajax, name = 'add_product_ajax'),
    # ex: remove_product/some_name
    path('remove_product/<str:product_name>', views.remove_product, name = 'remove_product'),
    # ex: remove_quantity/some_name
    path('remove_quantity/<str:product_name>', views.remove_quantity, name = 'remove_quantity'),
    # ex: create_order
    path('create_order/', views.create_order, name = 'create_order'),

    path('remove_product_ajax/', views.remove_product_ajax, name = 'remove_product_ajax'),
    path('remove_quantity_ajax/', views.remove_quantity_ajax, name = 'remove_quantity_ajax'),
    path('add_quantity_ajax/', views.add_quantity_ajax, name = 'add_quantity_ajax'),
    path('update_sum_ajax/', views.update_sum_ajax, name = 'update_sum_ajax'),
    path('update_cartsum_ajax/', views.update_cartsum_ajax, name = 'update_cartsum_ajax'),
    path('create_order_ajax/', views.create_order_ajax, name = 'create_order_ajax'),
    path('add_product_ajax_dvorniki/', views.add_product_ajax_dvorniki, name = 'add_product_ajax_dvorniki'),
    path('add_product_ajax_himiya/', views.add_product_ajax_himiya, name = 'add_product_ajax_himiya'),
    path('add_product_ajax_accessories/', views.add_product_ajax_accessories, name = 'add_product_ajax_accessories'),
    path('add_product_ajax_emergency/', views.add_product_ajax_emergency, name = 'add_product_ajax_emergency'),
    path('add_product_ajax_uhod/', views.add_product_ajax_uhod, name = 'add_product_ajax_uhod'),
]