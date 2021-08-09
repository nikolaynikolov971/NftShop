from django.contrib.auth import get_user_model

from shop.products.models import Product
from shop.profiles.models import Profile

UserModel = get_user_model()

class ProductTestUtils:
    def create_product(self, **kwargs):
        return Product.objects.create(**kwargs)


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.create_user(**kwargs)


class ProfileUtils:
    def create_profile(self, **kwargs):
        return Profile.objects.create(**kwargs)