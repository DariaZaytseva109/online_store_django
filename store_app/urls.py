"""URL маршруты"""
from django.urls import path

from store_app.views import main, categories, log_in, products, product_page

urlpatterns = [
    path('main/', main, name='main'),
    path('categories/', categories, name='categories'),
    path('log_in/', log_in, name='log_in'),
    path('products/', products, name='products'),
    path('products/<slug>', product_page, name='product_page'),
    ]
