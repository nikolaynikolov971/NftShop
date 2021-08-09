from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.mixins import ProductTestUtils
from tests.base.tests import ShopUserTestCase

UserModel = get_user_model()


class AddProductToCart(ProductTestUtils, ShopUserTestCase):
    def test_addProductToCart(self):
        self.client.force_login(self.user)

        self.product = self.create_product(
            title="Test",
            price=555.55,
            image='media/products/Dart.png',
            description="dasd",
            is_sold=False,

        )
        response = self.client.get(reverse('add_product_to_cart', kwargs={'pk': self.product.id}))

        self.assertEqual(302, response.status_code)
