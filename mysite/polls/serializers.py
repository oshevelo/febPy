from rest_framework import serializers
from .models import Question, Choice

    
class QuestionListSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text']


class QuestionDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'pub_date', 'question_text', 'was_published_recently']
        


