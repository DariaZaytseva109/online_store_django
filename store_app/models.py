from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=15, unique=True)
    # image = None
    price = models.IntegerField()
    subcategory = models.ForeignKey('Subcategory', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=15, unique=True)
    # image = None
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=15, unique=True)
    # image = None

    def __str__(self):
        return self.name
