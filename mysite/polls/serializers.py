from rest_framework import serializers
from .models import Question, Choice

    
class QuestionListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text']


class QuestionDetailsSerializer(serializers.ModelSerializer):
    choices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text', 'was_published_recently', 'choices']
        

class ChoiceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'votes']


class ChoiceDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'choice_description', 'votes']