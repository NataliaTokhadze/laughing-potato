from django.urls import path
from products.views import products_view, cart_view

urlpatterns = [
    path('products/', products_view, name='products'),
    path('cart/', cart_view, name='cart'),
]