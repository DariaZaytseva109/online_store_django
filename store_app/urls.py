from django.urls import path

from store_app.views import main, categories, basket, log_in, products

urlpatterns = [
    path('main/', main, name='main'),
    path('categories/', categories, name='categories'),
    path('basket/', basket, name='basket'),
    path('log_in/', log_in, name='log_in'),
    path('products/', products, name='products')
    ]