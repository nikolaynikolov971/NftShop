from django.contrib import admin

# Register your models here.
from shop.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'first_name', 'last_name']
