from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from categories.serializers import CategorySerializer, CategoryImageSerializer, CategoryDetailSerializer
from categories.models import Category, CategoryImage
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView

class CategoryViewSet(ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
class CategoryDetailViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]
    
class CategoryImageViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = self.queryset.filter(category=self.kwargs['category_id'])
        return queryset