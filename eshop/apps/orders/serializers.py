from rest_framework import serializers
from .models import Order, OrderItem
from apps.products.models import Product


# """ Nested serializer seems to be needed for OrderItem, because OrderItem is building block for the Order """
# """ Not clear whether method CREATE is required for model orders// """

class ProductNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Product
        read_only_fields = ['name', 'price', 'description']
        fields = read_only_fields + ['id']


class OrderItemDetailSerializer(serializers.ModelSerializer):
    product = ProductNestedSerializer()

    class Meta:
        model = Order
        fields = ['product', 'quantity']

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        validated_data.update({'product_id': product_data.get('id')})
        return OrderItem(**validated_data)

    def update(self, instance, validated_data):
        product_data = validated_data.pop('product')
        instance = super().update(instance, validated_data)
        instance.product_id = product_data.get('id')
        instance.save()
        return instance


class OrderItemNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderDetailSerializer(serializers.ModelSerializer):
    order_item = OrderItemNestedSerializer()

    class Meta:
        model = Order
        fields = ['id', 'order', 'date_created', 'last_updated', 'order_type', 'user', 'value', 'product']

    def create(self, validated_data):
        order_item_data = validated_data.pop('order_item')
        validated_data.update({'order_item_id': order_item_data.get('id')})
        return Order(**validated_data)

    def update(self, instance, validated_data):
        order_item_data = validated_data.pop('order_item')
        instance = super().update(instance, validated_data)
        instance.order_item_id = order_item_data.get('id')
        instance.save()
        return instance


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'order', 'date_created', 'last_updated', 'order_type', 'user', 'value']