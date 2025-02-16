from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from categories.serializers import CategorySerializer, CategoryImageSerializer, CategoryDetailSerializer
from categories.models import Category, CategoryImage
from rest_framework.permissions import IsAuthenticated
class CategoryListView(ListModelMixin,
                       GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk=None, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class CategoryDetailView(RetrieveModelMixin,
                       GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk=None, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class CategoryImageView(ListModelMixin, CreateModelMixin,
                       GenericAPIView):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = self.queryset.filter(category=self.kwargs['category_id'])
        return queryset
    
    def get(self, request, pk=None, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)