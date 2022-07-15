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


class ShipmentNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['delivery_company', 'delivery_office_number', 'addressee_last_name']


class OrderDetailSerializer(serializers.ModelSerializer):
    order_item = OrderItemNestedSerializer()
    shipment = ShipmentNestedSerializer()

    class Meta:
        model = Order
        fields = ['id', 'order', 'date_created', 'last_updated', 'order_type', 'user', 'value', 'product', 'shipment']

    def __parce_nested(self, validated_data, field_name, prop_name):
        order_item_data = validated_data.pop(field_name)
        validated_data.update({prop_name: order_item_data.get('id')})
        return validated_data

    def create(self, validated_data):
        validated_data = self.__parce_nested(validated_data, 'order_item', 'order_item_id')
        return Order.objects.create(**validated_data)

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


