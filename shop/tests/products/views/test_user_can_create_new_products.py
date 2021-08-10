from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from tests.base.tests import ShopUserTestCase

UserModel = get_user_model()


class ProfileDetailsTest(ShopUserTestCase):
    def test_userCantCreateProduct(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email='testt@abv.bg',
            password='staffstaff',

        )
        self.client.force_login(self.user)
        response = self.client.post(reverse('create_product'))
        self.assertEqual(403, response.status_code)

    def test_userCanCreateProduct(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email='testt@abv.bg',
            password='staffstaff',
            is_superuser=True

        )
        self.client.force_login(self.user)
        response = self.client.post(reverse('create_product'))
        self.assertEqual(200, response.status_code)