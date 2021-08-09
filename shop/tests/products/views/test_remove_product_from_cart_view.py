from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.mixins import ProductTestUtils
from tests.base.tests import ShopUserTestCase

UserModel = get_user_model()


class RemoveProductFromCartTest(ProductTestUtils, ShopUserTestCase):
    def test_RemoveProductFromCart(self):
        self.client.force_login(self.user)

        product = self.create_product(
            title="Test",
            price=555.55,
            image='media/products/Dart.png',
            description="dasd",
            is_sold=False,

        )
        response = self.client.get(reverse('remove_from_cart', kwargs={'pk': product.id}))

        self.assertEqual(302, response.status_code)