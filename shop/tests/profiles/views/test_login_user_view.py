from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from tests.base.tests import ShopUserTestCase

UserModel = get_user_model()


class ProfileDetailsTest(ShopUserTestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email='test@abv.bg',
            password='staffstaff',
        )

    def test_LogInUser(self):
        login = Client().login(email='test@abv.bg', password='staffstaff')
        self.assertTrue(login)

        response = self.client.post(reverse('login_user'))
        self.assertEqual(200, response.status_code)

