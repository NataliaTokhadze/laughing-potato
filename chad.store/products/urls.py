from django.urls import path
from products.views import (ProductViewSet,
                            ReviewViewSet,
                            CartViewSet,
                            # product_tag_view,
                            FavoriteProductViewSet)

urlpatterns = [
    path('products/', ProductViewSet.as_view(), name="products"),
    path('products/<int:pk>/', ProductViewSet.as_view(), name='product'),
    path('reviews/', ReviewViewSet.as_view(), name="reviews"),
    path('cart/', CartViewSet.as_view(), name='cart'),
    # path('products_tags', product_tag_view, name='products_tags'),
    path('favorite_products/', FavoriteProductViewSet.as_view(), name='favorite_products'),
    path('favorite_products/<int:pk>/', FavoriteProductViewSet.as_view(), name='favorite_product')
]