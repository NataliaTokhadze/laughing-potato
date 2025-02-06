from django.urls import path
from products.views import products_view, cart_view, product_tag_view, favorite_product_view

urlpatterns = [
    path('products/', products_view, name='products'),
    path('carts/', cart_view, name='carts'),
    path('products_tags', product_tag_view, name='products_tags'),
    path('favorite_products/', favorite_product_view, name='favorite_products'),
]