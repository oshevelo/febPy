from rest_framework import serializers
from apps.feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'user_email', 'user_phone', 'feedback_to', 'feedback', 'is_published']


class FeedbackDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'user_email', 'user_phone', 'feedback_to', 'feedback', 'is_published']
