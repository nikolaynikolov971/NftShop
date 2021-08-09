from django.contrib.auth import get_user_model
from django.test import Client
from tests.base.tests import ShopUserTestCase

UserModel = get_user_model()


class ProfileDetailsTest(ShopUserTestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email='test@abv.bg',
            password='staffstaff',
        )

    def test_creatingProfile_whenUserIsCreated(self):
        profile = self.user.profile

        self.assertEqual(self.user.id, profile.user_id)