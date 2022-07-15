from rest_framework import serializers
from .models import Cart, CartItem
from apps.products.models import Product
from eshop.settings import QUANTITY_LIMIT, TOTAL_PRICE_LIMIT


class ProductNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Product
        read_only_fields = [
            'sku',
            'name',
            'price',
            'amount_in_stock'
        ]
        fields = ['id'] + read_only_fields


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer()

    class Meta:
        model = CartItem
        fields = [
            'id',
            'cart',
            'product',
            'quantity',
            'cost_product'
        ]

    def validate(self, data):
        cart_items = CartItem.objects.filter(cart=data.get('cart'))
        product = Product.objects.get(pk=data.get('product').get('id'))
        if cart_items.count() >= QUANTITY_LIMIT:
            raise serializers.ValidationError(
                f'Limited product quantity in cart: {QUANTITY_LIMIT}'
            )
        if data.get('quantity', 0) > product.amount_in_stock:
            raise serializers.ValidationError(
                f'Products is available: {product.amount_in_stock}',
            )
        return data

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        validated_data.update({'product_id': product_data.get('id')})
        return CartItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'product' in validated_data:
            product_data = validated_data.pop('product')
            print(product_data)
            instance = super().update(instance, validated_data)
            instance.product_id = product_data.get('id')
            instance.save()
            return instance
        instance = super().update(instance, validated_data)
        return instance


class CartItemNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    product = ProductNestedSerializer(read_only=True)

    class Meta:
        model = CartItem

        read_only_fields = [
            'cart',
            'cost_product'
        ]

        fields = [
            'id',
            'cart',
            'product',
            'quantity',
            'cost_product'
        ]


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemNestedSerializer(many=True, read_only=True)

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
