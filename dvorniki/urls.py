from django.urls import path 
from . import views
    
app_name = 'dvorniki'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('mark/<int:mark_id>', views.mark, name = 'mark'),
    path('mark/<int:mark_id>/<int:model_id>', views.model, name = 'model'),
    path('gen/<int:mark_id>/<int:model_id>/<int:gen_id>', views.gen, name = 'gen'),
    path('product/<product_id>', views.product, name = 'product'),
]