from rest_framework import serializers
from .models import Order, OrderItem

#""" Nested serializer seems to be needed for OrderItem, because OrderItem is building block for the Order """
#""" Not clear whether method CREATE is required for model orders// """

class OrderItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'order', 'quantity']


class OrderItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity']


class OrderItemNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']
        read_only_fields = ['product', 'quantity']


class OrderListSerializer(serializers.ModelSerializer):
    order = OrderItemNestedSerializer()

    class Meta:
        model = Order
        fields = ['id', 'order', 'date_created', 'order_type', 'user', 'value', 'shipment']

    def create(self, validated_data):
        order_item_data = validated_data.pop('order_item')
        validated_data.update({'order_item_id': order_item_data.get('id')})
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        order_item_data = validated_data.pop('order_item')
        validated_data.update({'order_item_id': order_item_data.get('id')})
        return Order.objects.create(**validated_data)


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'date_created', 'order_type', 'user', 'value', 'shipment']

