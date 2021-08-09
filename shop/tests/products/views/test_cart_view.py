from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.mixins import ProductTestUtils
from tests.base.tests import ShopUserTestCase

UserModel = get_user_model()


class CartView(ProductTestUtils, ShopUserTestCase):
    def test_emptyCart(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('cart'))

        products = list(response.context['products'])

        self.assertEqual(200, response.status_code)
        self.assertListEmpty(products)


    def test_CartWithProducts(self):
        self.client.force_login(self.user)

        self.product = self.create_product(
            title="Test",
            price=555.55,
            image='media/products/Dart.png',
            description="dasd",
            is_sold=False,
            user=self.user

        )

        self.second_product = self.create_product(
            title="Test2",
            price=555.55,
            image='media/products/Dart.png',
            description="dasd",
            is_sold=False,
            user=self.user

        )

        response = self.client.get(reverse('cart'))
        products = list(response.context['products'])

        self.assertEqual(200, response.status_code)
        self.assertEqual(1111.10, sum([p.price for p in products]))
        self.assertListEqual(products, [self.product, self.second_product])