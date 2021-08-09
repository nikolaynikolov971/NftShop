from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
from shop.shop_auth.managers import ShopUserManager


class ShopUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = ShopUserManager()


from .signals import *
