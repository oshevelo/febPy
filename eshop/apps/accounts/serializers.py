from .models import Rating,Discount,PointCount
from rest_framework import serializers

class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user','percentile']

class DiscountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['user','points','pointcount','discount','prevcount']

class PointCountModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = PointCount
            fields = ['user','points']