from rest_framework import serializers
from .models import Question, Choice


    
class QuestionListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'length', 'question_text']


class QuestionDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'pub_date',  'question_text', 'length', 'was_published_recently']
        
    def validate(self, data):
        print('validate')
        if data.get('length') == 10 and 'zxc' not in data.get('question_text'):
            raise serializers.ValidationError('"zxc" not in question_text when length=10')
        return data
        
    def validate_length(self, data):
        print('field length')
        errors = []
        if data % 2 != 0:
            errors.append('length must be even')
        if data == 3:
            errors.append('length !=3')
        if errors:
            raise serializers.ValidationError(errors)
        return data
        
    def validate_question_text(self, data):
        print('field question_text')
        
        return data
        
            
class QuestionNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    
    class Meta:
        model = Question
        read_only_fields = ['pub_date', 'question_text']
        fields = read_only_fields + ['id']
        
        
class ChoiceListSerializer(serializers.ModelSerializer):
    question = QuestionNestedSerializer()
    
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'choice_description']
        
    def __parce_nested(self, validated_data, field_name, prop_name):
        question_data = validated_data.pop(field_name)
        validated_data.update({prop_name: question_data.get('id')})
        return validated_data
        
    def create(self, validated_data):
        validated_data = self.__parce_nested(validated_data, 'question', 'question_id')
        return Choice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        question_data = validated_data.pop('question')
        instance = super().update(instance, validated_data)
        instance.question_id = question_data.get('id')
        instance.save()
        return instance
