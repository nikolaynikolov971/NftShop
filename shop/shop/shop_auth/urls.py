from django.urls import path

from shop.shop_auth.views import login_user, register_user, logout_user

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('logout/', logout_user, name='logout_user')
]

