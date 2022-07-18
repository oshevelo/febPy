from rest_framework import serializers
from .models import PaymentSystemLog, Payment
from django.contrib.auth.models import User


class PaymentNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    owner = serializers.ReadOnlyField(source='owner.username')
    editor = serializers.ReadOnlyField(source='editor.username')

    class Meta:
        model = Payment
        fields = ['owner', 'editor', 'id', 'system', 'status', 'products_price', 'delivery_price']
        read_only_fields = ['owner', 'editor', 'system', 'status', 'products_price', 'delivery_price']


class PaymentSystemLogSerializer(serializers.ModelSerializer):
    payment = PaymentNestedSerializer()

    class Meta:
        model = PaymentSystemLog
        fields = ['id', 'payment', 'request_data', 'response_data', 'created_at', 'updated_at']

    def __parce_nested(self, validated_data, field_name, prop_name):
        payment_data = validated_data.pop(field_name)
        validated_data.update({prop_name: payment_data.get('id')})
        return validated_data

    def create(self, validated_data):
        validated_data = self.__parce_nested(validated_data, 'payment', 'payment_id')
        return PaymentSystemLog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data = self.__parce_nested(validated_data, 'payment', 'payment_id')
        return PaymentSystemLog.objects.create(**validated_data)


class PaymentListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    editor = serializers.ReadOnlyField(source='editor.username')

    class Meta:
        model = Payment
        fields = ['owner', 'editor', 'id', 'system', 'status', 'products_price', 'delivery_price']

    def validate(self, data):
        if data.get('delivery_price') > data.get('products_price'):
            raise serializers.ValidationError('delivery is higher than the product price')
        return data
