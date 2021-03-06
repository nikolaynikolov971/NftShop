from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class ShopUserTestCase(TestCase):
    logged_in_user_email = 'test@abv.bg'
    logged_in_user_password = 'staffstaff'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )

    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')
