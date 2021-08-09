from django.urls import path

from shop.products.views import ShowProductsListView, product_details, CreateProductView, \
    DeleteProductView, cart, AboutUsView, ContactUsView, add_product_to_cart, \
    remove_product_from_cart, SearchProductView, check_out, update_product, show_bought_products

urlpatterns = [
    path('products/', ShowProductsListView.as_view(), name='all_products'),
    path('about/', AboutUsView.as_view(), name='about_us'),
    path('contact_us', ContactUsView.as_view(), name='contact_us'),
    path('cart/', cart, name='cart'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('update_product/<int:pk>/', update_product, name='update_product'),
    path('delete_product/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
    path('product_details/<int:pk>/', product_details, name='product_details'),
    path('add_to_cart/<int:pk>', add_product_to_cart, name='add_product_to_cart'),
    path('remove_from_cart/<int:pk>', remove_product_from_cart, name='remove_from_cart'),
    path('searched_product/', SearchProductView.as_view(), name='searched_product'),
    path('checkout/', check_out, name='check_out'),
    path('bought_products/', show_bought_products, name='bought_products')


]