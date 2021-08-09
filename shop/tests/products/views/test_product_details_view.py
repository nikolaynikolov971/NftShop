from django.test import TestCase, Client
from django.urls import reverse

from shop.products.models import Product
from tests.base.mixins import ProductTestUtils


class ProductDetailsTest(ProductTestUtils, TestCase):
    def setUp(self):
        self.client = Client()
        self.product = self.create_product(
            title="Barry",
            price=555.55,
            image='media/products/Dart.png',
            description="dasd",
            is_sold=False,

        )

    def test_getProductDetails(self):
        response = self.client.get(reverse('product_details', kwargs={'pk': self.product.id}))

        self.assertEqual(200, response.status_code)

    def test_showErrorIfProductDoesNotExist(self):
        try:
            self.client.get(reverse('product_details', kwargs={'pk': self.product.id}))
        except Product.DoesNotExist:
            self.assertRaises(Exception)
