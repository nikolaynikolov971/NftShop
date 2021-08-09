from django.db.models.signals import pre_save
from django.dispatch import receiver

from shop.profiles.models import Profile


@receiver(pre_save, sender=Profile)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.address and instance.city and instance.phone_number:
        instance.is_completed = True

