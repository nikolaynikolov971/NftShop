from django.urls import path

from shop.profiles.views import home_page, my_profile, profile_details, ShowAllProfiles

urlpatterns = [
    path('', home_page, name='landing_page'),
    path('my_profile/', my_profile, name='my_profile'),
    path('profile_details', profile_details, name='profile_details'),
    path('all_profiles/', ShowAllProfiles.as_view(), name='all_profiles')


]


import shop.profiles.signals