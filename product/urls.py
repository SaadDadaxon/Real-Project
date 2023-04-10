from django.urls import path
from .views import product_views, product_detail

app_name = 'product'

urlpatterns = [
    path('products/', product_views, name='index'),
    path('products/<int:pk>/', product_detail, name='detail'),
]
