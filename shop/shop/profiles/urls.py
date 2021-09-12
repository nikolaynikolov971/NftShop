from django.urls import path

from shop.profiles.views import home_page, my_profile, profile_details, show_all_profiles

urlpatterns = [
    path('', home_page, name='landing_page'),
    path('my_profile/', my_profile, name='my_profile'),
    path('profile_details', profile_details, name='profile_details'),
    path('all_profiles/', show_all_profiles, name='all_profiles')


]


import shop.profiles.signals