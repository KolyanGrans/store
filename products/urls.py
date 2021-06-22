from django.urls import path
from .views import *


app_name = 'products'


urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('page/<int:page>/', products, name='page'),
    path('products/<int:category_id>/', products, name='category'),
    path('basket_add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket_del/<int:id>/', basket_del, name='basket_del')
]