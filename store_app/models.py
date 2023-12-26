"""Определяем модели"""
from django.db import models


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование'
    )
    slug = models.SlugField(max_length=15, unique=True)
    # image = None
    price = models.IntegerField(verbose_name='Цена')
    subcategory = models.ForeignKey(
        'Subcategory',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Подкатегория')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"


class Subcategory(models.Model):
    """Модель подкатегории"""
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Наименование')
    slug = models.SlugField(max_length=15, unique=True)
    # image = None
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Подкатегории"
        verbose_name_plural = "Подкатегории"


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Наименование'
    )
    slug = models.SlugField(max_length=15, unique=True)
    # image = None

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
