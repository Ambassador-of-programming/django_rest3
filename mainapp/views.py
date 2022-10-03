from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from mainapp.serializers import(
    Cart, CartProduct, Product, ProductSerializer, CartSerializer, CartProductSerializer
)

# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartProductViewSet(ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

