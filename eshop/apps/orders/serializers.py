from rest_framework import serializers
from .models import Order, OrderItem
from apps.products.models import Product


# """ Nested serializer seems to be needed for OrderItem, because OrderItem is building block for the Order """
# """ Not clear whether method CREATE is required for model orders// """

class ProductNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Product
        read_only_fields = ['id', 'name', 'price', 'description'] #"sku" or "id"


class OrderItemDetailSerializer(serializers.ModelSerializer):
    products = ProductNestedSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['products', 'quantity']

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        validated_data.update({'products_id': products_data.get('id')})
        return OrderItem.products.create(**validated_data)

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products')
        instance.products_id = products_data.get('id')
        instance.save()
        return instance


class OrderItemNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        read_only_fields = ['products', 'quantity']


class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order', 'date_created', 'last_updated', 'order_type', 'user', 'value', 'products']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        validated_data.update({'order_items_id': order_items_data.get('id')})
        return Order.order_items.create(**validated_data)


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'order', 'date_created', 'last_updated', 'order_type', 'user', 'value']