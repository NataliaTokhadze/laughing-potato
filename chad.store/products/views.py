from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product, Cart, ProductTag 
from products.serializers import ProductSerializer, CartSerializer, ProductTagSerializer

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
        product_tags = ProductTag.objects.all()
        product_tag_list = []

        for product_tag in product_tags:
            product_tag_data = {
                'id': product_tag.id,
                'user_id': product_tag.id,
            }
            product_tag_list.append(product_tag.data)

        return Response({'cart': product_tag.data})
    
    elif request.method == 'POST':
        data = request.data 
        serializer = ProductTagSerializer(data=data)
        if serializer.is_valid():
            created_cart = Cart.objects.create(
                quantity=data.get('quantity'),
            )
            return Response({'id':created_cart.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)