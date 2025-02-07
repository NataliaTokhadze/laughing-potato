from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from products.models import Product, Review, Cart, ProductTag, FavoriteProduct
from products.serializers import ProductSerializer, ReviewSerializer, CartSerializer, ProductTagSerializer, FavoriteProductSerializer


class ProductListCreateView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({"id": product.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ProductDetailView(APIView):
    def get(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(obj)
        return Response(serializer.data)
    
    def put(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def reviews_view(request):
    if request.method == "GET":
        serializer = ReviewSerializer(Review.objects.all(), many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)  
        if serializer.is_valid():
            product = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])  
def cart_view(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CartSerializer(data=request.data)  
        if serializer.is_valid():
            cart = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def product_tag_view(request):
    if request.method == 'GET':
        products_tags = ProductTag.objects.all()
        serializer = ProductTagSerializer(products_tags, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductTagSerializer(data=request.data)  
        if serializer.is_valid():
            product_tag = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def favorite_product_view(request):
    if request.method == 'GET':
        favorite_products = FavoriteProduct.objects.all()
        serializer = FavoriteProductSerializer(favorite_products, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = FavoriteProductSerializer(data=request.data)  
        if serializer.is_valid():
            favorite_product = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)