from itertools import product
from rest_framework import serializers

from mainapp.models import(
    Product, Cart, CartProduct
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'articul', )


class CartSerializer(serializers.ModelSerializer):
    product = serializers.ListField()
    class Meta:
        model = Cart
        fields = ('id', 'user_name', 'created_at', 
        'total_price', 'delivery_address', )
    read_only_fields = ('created_at', )

    def create(self, validated_data):
        cart = Cart.objects.create(
            user_name = validated_data.get('user_name'),
            delivery_address = validated_data.get('delivery_address')
        )

        for p in validated_data.get('product'):
            CartProduct.objects.create(
                product=Product.objects.filter(id=p.get('id')).first(),
                cart=cart,
                amount=p.get('amount'),
            )
        cart.total_price = sum([p.sum_product_price for p in cart.cart_product.all()])
        cart.save()
        return cart

    # [
    #     {'id': 1, 'amout': 10},
    #     {'id': 1, 'amout': 10},
    #     {'id': 1, 'amout': 10},
    #     {'id': 1, 'amout': 10},
    #     {'id': 1, 'amout': 10},
    # ]



class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('id', 'product', 'cart', 'total_price', 'amount', )