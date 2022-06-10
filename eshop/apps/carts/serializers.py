from rest_framework import serializers
from .models import Cart, CartItem


class CartItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = [
            'id',
            'cart',
            'product',
            'user',
            'product_name',
            'quantity',
            'product_quantity_available',
            'cost_product'
        ]


class CartItemDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = [
            'id',
            'cart',
            'product',
            'user',
            'product_sku',
            'product_name',
            'unit_price',
            'quantity',
            'product_quantity_available',
            'cost_product'
        ]


class CartListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'cart_list',
            'total_price'
        ]


class CartDetailsSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    cart_items = CartItemDetailsSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'cart_items',
            'total_price',
            'created',
            'updated'
        ]
