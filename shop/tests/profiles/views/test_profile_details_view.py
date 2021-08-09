from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.tests import ShopUserTestCase

UserModel = get_user_model()


class ProfileDetailsTest(ShopUserTestCase):
    def test_getProfileDetails(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile_details'))

        profile = self.user.profile

        self.assertEqual(self.user.id, profile.user_id)
        self.assertEqual(200, response.status_code)

    def test_postProfileDetails(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('profile_details'))

        self.assertEqual(302, response.status_code)
