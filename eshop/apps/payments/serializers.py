from rest_framework import serializers
from .models import PaymentSystemLog, Payment
from django.contrib.auth.models import User


class PaymentSystemLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentSystemLog
        fields = ['id', 'payment', 'request_data', 'response_data', 'created_at', 'updated_at']


class PaymentListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    editor = serializers.ReadOnlyField(source='editor.username')

    class Meta:
        model = Payment
        fields = ['owner', 'editor', 'id', 'system', 'status', 'products_price', 'delivery_price']

