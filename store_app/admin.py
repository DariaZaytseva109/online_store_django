from django.contrib import admin

from .models import Product, Subcategory, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'subcategory']
    list_display_links = ['name']
    list_per_page = 10
    search_fields = ['name']


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_display_links = ['name']
    list_per_page = 10
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Category, CategoryAdmin)
