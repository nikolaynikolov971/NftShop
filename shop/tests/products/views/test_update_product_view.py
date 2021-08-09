from django.test import TestCase, Client

from django.urls import reverse

from tests.base.mixins import ProductTestUtils


class UpdateProductDetails(ProductTestUtils, TestCase):
    def setUp(self):
        self.client = Client()
        self.product = self.create_product(
            title="Test",
            price=555.55,
            image='media/products/Dart.png',
            description="dasd",
            is_sold=False,

        )


    def test_postUpdateProduct(self):
        response = self.client.post(reverse('update_product', kwargs={'pk': self.product.id}))

        self.assertEqual(302, response.status_code)
