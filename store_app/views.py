"""Views определяем"""

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from store_app.models import Category, Subcategory, Product

main_menu = [
    {'title': 'На главную', 'url_name': 'main'},
    {'title': 'Категории', 'url_name': 'categories'},
    {'title': 'Продукты', 'url_name': 'products'},
    {'title': 'Войти', 'url_name': 'log_in'}
    ]


def main(request):
    data = {'page_title': "Главная", 'menu': main_menu}
    return render(request, 'store_app/main.html', context=data)


def categories(request):
    cats = Category.objects.all()
    subcats = Subcategory.objects.all()
    paginator = Paginator(cats, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    data = {'page_title': "Категории", 'menu': main_menu, 'cats': page, 'subcats': subcats}
    return render(request, 'store_app/categories.html', context=data)


def products(request):
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    data = {'page_title': "Продукты", 'menu': main_menu, 'page': page}
    return render(request, 'store_app/products.html', context=data)


def product_page(request, slug):
    product = Product.objects.filter(slug=slug).first()
    page_title = product.name
    data = {'product': product, 'menu': main_menu, 'page_title': page_title}
    return render(request, 'store_app/product_page.html', context=data)


# def basket(request):
    #     data = {'page_title': "Корзина", 'menu': main_menu}
    # return render(request, 'store_app/products.html', context=data)


def log_in(request):
    data = {'page_title': "Вход", 'menu': main_menu}
    return render(request, 'store_app/log_in.html', context=data)
