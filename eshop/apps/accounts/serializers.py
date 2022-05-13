from .models import Rating,Discount,PointCount
from rest_framework import serializers


class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields = ['_user_id','_percentile']


class DiscountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['_user_id', 'user_point','_user_discount']


class PointCountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointCount
        fields = ['_user_id', '_points']


