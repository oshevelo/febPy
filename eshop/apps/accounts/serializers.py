from .models import Rating,Discount,PointCount
from rest_framework import serializers


class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields = ['_user_id','_percentile']

class RatingListSerializer(serializers.ListSerializer):
    class Meta:
        model=Rating
        fields = ['_user_id','_percentile']


class DiscountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['_user_id', 'user_point','_user_discount']


class DiscountListSerializer(serializers.ListSerializer):
    class Meta:
        model = Discount
        fields = ['_user_id', '_user_point','_user_discount']


class PointCountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointCount
        fields = ['_user_id', '_points']


class PointCountListSerializer(serializers.ListSerializer):
    class Meta:
        model = PointCount
        fields = ['_user_id', '_percentile']
