from rest_framework import serializers
from .models import PaymentSystemLog, Payment
from django.contrib.auth.models import User


class PaymentSystemLogSerializer(serializers.ModelSerializer):


    class Meta:
        model = PaymentSystemLog
        fields = ['id', 'payment', 'request_data', 'response_data', 'created_at', 'updated_at']

    # def create(self, validated_data):
    #



class PaymentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ['id', 'system', 'status', 'products_price', 'delivery_price']



