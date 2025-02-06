from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product, Cart, ProductTag, FavoriteProduct
from products.serializers import ProductSerializer, CartSerializer, ProductTagSerializer, FavoriteProductSerializer

@api_view(['GET', 'POST'])
def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_list = []
        
        for product in products:
            product_data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'currency': product.currency,
                'quantity': product.quantity,
            }
            products_list.append(product_data)
        
        return Response({'products': products_list})
    elif request.method == 'POST':
        data = request.data 
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            created_product = Product.objects.create(
                name=data.get('name'),
                description=data.get('description'),
                price=data.get('price'),
                currency=data.get('currency'),
                quantity=data.get('quantity'),
            )
            return Response({'id':created_product.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)
        
@api_view(['GET', 'POST'])  
def cart_view(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        carts_list = []

        for cart in carts:
            cart_data = {
                'id': cart.id,
                'quantity': cart.quantity,
            }
            carts_list.append(cart_data)

        return Response({'cart': carts_list})
    
    elif request.method == 'POST':
        data = request.data 
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            created_cart = Cart.objects.create(
                quantity=data.get('quantity'),
            )
            return Response({'id':created_cart.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)

@api_view(['GET', 'POST'])
def product_tag_view(request):
    if request.method == 'GET':
        products_tags = ProductTag.objects.all()
        products_tags_list = []
        
        for product in products_tags:
            product_tag_data = {
                'product_id': product.id,
                'tag_name': product.tag_name,
            }
            products_tags_list.append(product_tag_data)
        
        return Response({'products_tags': products_tags_list})
    elif request.method == 'POST':
        data = request.data 
        serializer = ProductTagSerializer(data=data)
        if serializer.is_valid():
            created_product_tag = ProductTag.objects.create(
                tag_name=data.get('tag_name'),
            )
            return Response({'id':created_product_tag.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)

@api_view(['GET', 'POST'])
def favorite_product_view(request):
    if request.method == 'GET':
        favorite_products = Product.objects.all()
        favorite_products_list = []
        
        for favorite_product in favorite_products:
            favorite_product_data = {
                'product_id': favorite_product.id,
                'user_id': favorite_product.id,
            }
            favorite_products_list.append(favorite_product_data)
        
        return Response({'favorite_products': favorite_products_list})
    elif request.method == 'POST':
        data = request.data 
        serializer = FavoriteProductSerializer(data=data)
        if serializer.is_valid():
            created_favorite_product = FavoriteProduct.objects.create(
                product_id=data.get('product_id'),
                user_id=data.get('user_id'),
            )
            return Response({'id':created_favorite_product.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)
