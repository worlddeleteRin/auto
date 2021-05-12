from django.urls import path 
from . import views
    
app_name = 'lamp'

urlpatterns = [
    path('', views.index, name = 'index'),
    # ex: cars/Audi
    path('cars/<str:car_mark>', views.mark, name = 'mark'),
    # ex: cars/Audi/A4
    path('cars/<str:car_mark>/<str:car_model>', views.model, name='model'),
    # ex: cars/Audi/A4/5gen
    path('cars/<str:car_mark>/<str:car_model>/<str:car_gen>', views.gen, name = 'gen'),
    # ex: cars/Audi/A4/5gen/destination/category
    path('cars/<str:car_mark>/<str:car_model>/<str:car_gen>/<str:dest>/<str:cat>', views.car_lamps, name = 'car_lamps'),
    # ex: product/product_name
    path('product/<str:product_name>', views.product, name='product'),

    # ex: /category
    path('category/<str:cat>', views.category, name = 'category'),
    # ex: /types/h1/category
    path('types/<str:type>/<str:cat>', views.lamps_type, name='lamps_type'),
    # ex: /brands/bosch/category
    path('brands/<str:brand>/<str:cat>',views.brand, name='brand'),
    # ex: /brands
    path('brands/', views.allbrands, name = 'allbrands'),
    # ex: /brands/philips
    path('brands/<str:brand>', views.spesbrand, name = 'spesbrand'),
    # ex: /search
    path('search/', views.search, name='search'),
    
    path('ajax/form_car/', views.form_car_ajax, name="form_car_ajax"),
    path('form_car/', views.form_car, name="form_car"),

    path('filter_update_lamps/', views.filter_update_lamps, name='filter_update_lamps'),
    # about us page
    path('about_us', views.about_us, name = 'about_us'),
    # delivery page
    path('delivery', views.delivery, name = 'delivery'),
    # contact page
    path('contacts', views.contacts, name = 'contacts'),
]
