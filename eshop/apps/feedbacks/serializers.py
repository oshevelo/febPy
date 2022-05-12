from rest_framework import serializers
from apps.feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user_email', 'user_phone', 'feedback', 'is_published', 'is_deleted']


class FeedbackDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user_email', 'user_phone', 'feedback', 'is_published', 'is_deleted']
