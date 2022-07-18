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

    def __parse_nested(selfself, validated_data, field_name, prop_name):
        pointcount_data = validated_data.pop(field_name)
        validated_data.update({prop_name: pointcount_data.get("id")})
        return validated_data

    def create(self, validated_data):
        validated_data = self.__parse_nested(validated_data, 'pointcount', 'pointcount_id')
        return Rating.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pointcount_data = validated_data.pop('pointcount')
        instance = super().update(instance, validated_data)
        instance.question_id = pointcount_data.get('id')
        instance.save()

    #def validate(self,data):
     #  if data.get("percentile") > 1 or data.get('percentile') < 0:
      #     raise serializers.ValidationError("Improper value. percentile must be between 0 and 1")
       #return data

class DiscountModelSerializer(serializers.ModelSerializer):
    pointcount = PointCountNestedSerializer()

    class Meta:
        model = Discount
        fields = ['user', 'pointcount', 'discount', 'prev_count']

    def __parse_nested(self, validated_data, field_name, prop_name):
        pointcount_data = validated_data.pop(field_name)
        validated_data.update({prop_name: pointcount_data.get("id")})
        return validated_data

    def create(self, validated_data):
        validated_data = self.__parse_nested(validated_data, 'pointcount', 'pointcount_id')
        return Discount.objects.create(**validated_data)

    def update(self, instance, validated_data):
        question_data = validated_data.pop('pointcount')
        instance = super().update(instance, validated_data)
        instance.question_id = question_data.get('id')
        instance.save()


class PointCountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointCount
        fields = ['user', 'points']
