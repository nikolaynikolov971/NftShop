from django.contrib.auth import get_user_model
from django.urls import reverse


from tests.base.mixins import ProductTestUtils
from tests.base.tests import ShopUserTestCase

UserModel = get_user_model()


class ShowBoughtProductsPageTest(ProductTestUtils, ShopUserTestCase):

    def test_showBoughtProducts(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('bought_products'))

        self.assertEqual(200, response.status_code)
