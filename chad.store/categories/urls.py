from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter, DefaultRouter
from categories.views import (CategoryListViewSet,
                              CategoryDetailViewSet,
                              CategoryImageViewSet,)

router = routers.DefaultRouter()
router.register('categories', CategoryListViewSet)

categories_router = routers.NestedDefaultRouter(
    router,
    'categories',
    lookup='category'
)
categories_router.register('images', CategoryImageViewSet, basename='category_images')
categories_router.register('details', CategoryDetailViewSet, basename='category_details')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(categories_router.urls)),
]