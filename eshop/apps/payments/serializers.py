from rest_framework import serializers
from .models import PaymentSystemLog, Payment
from django.contrib.auth.models import User


class PaymentSystemLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentSystemLog
        fields = ['id', 'payment', 'request_data', 'response_data', 'created_at', 'updated_at']


class PaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['url', 'id', 'payment_system', 'payment_status', 'products_price', 'delivery_price']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']

