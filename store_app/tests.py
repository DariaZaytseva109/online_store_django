"""Create your tests here."""

from django.test import TestCase

from store_app.models import Product, Subcategory, Category


class ProductTestCase(TestCase):
    """тестовый класс"""
    # pylint: disable=no-member
    def setUp(self):
        """create test models"""
        cat_1 = Category.objects.create(
            name="Сладости",
            slug="sladosty",
        )
        cat_2 = Category.objects.create(
            name="Фрукты",
            slug="frukty",
        )
        sub_1 = Subcategory.objects.create(
            name="Конфеты",
            slug="konfety",
            category=cat_1
        )
        sub_2 = Subcategory.objects.create(
            name="Апельсины",
            slug="apelsiny",
            category=cat_2
        )
        Product.objects.create(
            name="Конфеты Коровка",
            slug="korovka",
            price=100,
            subcategory=sub_1
        )
        Product.objects.create(
            name="Апельсины крупные Египет",
            slug="apelsiny-krupnie",
            price=120,
            subcategory=sub_2
        )

    def test_categories(self):
        """testing created categories"""
        subcat = Subcategory.objects.filter(name='Апельсины').first()
        cat = Category.objects.filter(name='Фрукты')
        self.assertEqual(subcat.category, cat)
