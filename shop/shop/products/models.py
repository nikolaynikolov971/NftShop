from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from shop.products.validators import is_alpha_or_space_validator

UserModel = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=20, validators=[is_alpha_or_space_validator])
    price = models.FloatField()
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    is_sold = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

