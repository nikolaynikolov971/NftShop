from django.test import TestCase, Client

from shop.products.models import Product
from tests.base.mixins import ProductTestUtils


class SearchProduct(ProductTestUtils, TestCase):
    def test_Searched_Product_Found(self):
        self.client = Client()
        self.product = self.create_product(
            title="Test",
            price=555.55,
            image='media/products/Dart.png',
            description="dasd",
            is_sold=False,

        )

        db_queryset = Product.objects.filter(id=self.product.id)
        product = db_queryset[0]

        self.assertEqual(self.product, product)

    def test_Searched_Product_Not_Found(self):
        self.client = Client()
        self.product = Product(
            title="Test",
            price=555.55,
            image='media/products/Dart.png',
            description="dasd",
            is_sold=False,

        )

        db_queryset = Product.objects.all()
        searched_product = [p for p in db_queryset if p.title == self.product.title]

        self.assertNotEqual(self.product, searched_product)