from rest_framework import serializers
from .models import PaymentSystemLog, Payment
from django.contrib.auth.models import User


class PaymentNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Payment
        fields = ['owner', 'editor', 'id', 'system', 'status', 'products_price', 'delivery_price']
        read_only_fields = ['owner', 'editor', 'system', 'status', 'products_price', 'delivery_price']


class PaymentSystemLogSerializer(serializers.ModelSerializer):
    payment = PaymentNestedSerializer()

    class Meta:
        model = PaymentSystemLog
        fields = ['id', 'payment', 'request_data', 'response_data', 'created_at', 'updated_at']

    def create(self, validated_data):
        payment_data = validated_data.pop('payment')
        validated_data.update({'payment_id': payment_data.get('id')})
        return PaymentSystemLog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        payment_data = validated_data.pop('payment')
        validated_data.update({'payment_id': payment_data.get('id')})
        return PaymentSystemLog.objects.create(**validated_data)


class PaymentListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    editor = serializers.ReadOnlyField(source='editor.username')

    class Meta:
        model = Payment
        fields = ['owner', 'editor', 'id', 'system', 'status', 'products_price', 'delivery_price']

