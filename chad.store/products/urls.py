from django.urls import path
from products.views import (ProductViewSet,
                            ReviewViewSet,
                            cart_view,
                            product_tag_view,
                            favorite_product_view)

urlpatterns = [
    path('products/', ProductViewSet.as_view(), name="products"),
    path('products/<int:pk>/', ProductViewSet.as_view(), name='product'),
    path('reviews/', ReviewViewSet.as_view(), name="reviews"),
    path('carts/', cart_view, name='carts'),
    path('products_tags', product_tag_view, name='products_tags'),
    path('favorite_products/', favorite_product_view, name='favorite_products')
]