from django.db import models


# Create your models here.
from shop.shop_auth.models import ShopUser
from .validators import only_letters_validator, only_digits_validator


class Profile(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    address = models.TextField(max_length=200, blank=True)
    city = models.CharField(max_length=30, blank=True, validators=[only_letters_validator])
    phone_number = models.CharField(max_length=30, blank=True, validators=[only_digits_validator])
    is_completed = models.BooleanField(default=False)
    user = models.OneToOneField(ShopUser, on_delete=models.CASCADE, primary_key=True)

from .signals import *