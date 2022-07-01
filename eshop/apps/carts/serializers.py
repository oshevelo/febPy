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
        if data.get('quantity') > product.amount_in_stock:
            raise serializers.ValidationError(
                f'Products is available: {product.amount_in_stock}',
            )
        return data

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        validated_data.update({'product_id': product_data.get('id')})
        return CartItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        product_data = validated_data.pop('product')
        instance = super().update(instance, validated_data)
        instance.product_id = product_data.get('id')
        instance.save()

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
    cart_items = CartItemNestedSerializer(many=True)

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

    def create(self, validated_data):
        cart_items_data = validated_data.pop('cart_items')
        cart = Cart.objects.create(**validated_data)
        for item_data in cart_items_data:
            Cart.objects.create(**item_data, cart=cart)
        return cart

    def update(self, instance, validated_data):
        print(validated_data)
        cart_items = validated_data.pop('cart_items')
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        list_cart_items = []
        for item_data in cart_items:
            if 'id' in item_data.keys():
                if CartItem.objects.filter(id=item_data['id']).exists():
                    cart_item = CartItem.objects.get(id=item_data['id'])
                    cart_item.product = item_data.get('product', cart_item.product)
                    cart_item.quantity = item_data.get('quantity', cart_item.quantity)
                    cart_item.save()
                    list_cart_items.append(cart_item.id)
                else:
                    continue
            else:
                cart_item = CartItem.objects.create(**item_data, cart=instance)
                list_cart_items.append(cart_item.id)

        return instance
