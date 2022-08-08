from .models import Rating, Discount, PointCount
from rest_framework import serializers


class PointCountNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = PointCount
        read_only_fields = ['points']
        fields = read_only_fields + ['id']


class RatingModelSerializer(serializers.ModelSerializer):
    pointcount = PointCountNestedSerializer()

    class Meta:
        model = Rating
        fields = ['user', 'percentile', 'pointcount']

    def __parce_nested(selfself, validated_data, field_name, prop_name):
        pointcount_data = validated_data.pop(field_name)
        validated_data.update({prop_name: pointcount_data.get("id")})
        return validated_data

    def create(self, validated_data):
        validated_data = self.__parce_nested(validated_data, 'pointcount', 'pointcount_id',)
        return Rating.objects.create(**validated_data)

    def update(self, instance,validated_data):
        pointcount_data = validated_data.pop('pointcount', None)
        instance = super().update(instance, validated_data)
        if pointcount_data:
            instance.pointcount_id = pointcount_data.get('id')
            instance.save()
        return instance


class DiscountModelSerializer(serializers.ModelSerializer):
    pointcount = PointCountNestedSerializer()
    class Meta:
        model = Discount
        fields = ['user', 'pointcount', 'discount', 'prev_count']

    def __parce_nested(self, validated_data, field_name, prop_name):
        pointcount_data = validated_data.pop(field_name)
        validated_data.update({prop_name: pointcount_data.get("id")})
        return validated_data

    def create(self, validated_data):
        validated_data = self.__parce_nested(validated_data, 'pointcount', 'pointcount_id')
        return Discount.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pointcount_data = validated_data.pop('pointcount', None)
        instance = super().update(instance, validated_data)
        if pointcount_data:
            instance.pointcount_id = pointcount_data.get('id')
            instance.save()
        return instance


class PointCountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointCount
        fields = ['user', 'points']