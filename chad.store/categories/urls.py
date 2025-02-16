from django.urls import path
from categories.views import (CategoryListView,
                              CategoryDetailView,
                              CategoryImageView,)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name="categories"),
    path('categories/<int:pk>/', CategoryListView.as_view(), name='category'),
    path('categories/<int:category_id>/images/', CategoryImageView.as_view(), name='images'),
    path('categories/<int:product_id>/images/<int:pk>', CategoryImageView.as_view(), name='image')
]