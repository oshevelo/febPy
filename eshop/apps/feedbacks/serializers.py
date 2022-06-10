from rest_framework import serializers
from apps.feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'user_email', 'user_phone', 'subject', 'feedback', 'is_published']


class FeedbackDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'user_email', 'user_phone', 'subject', 'feedback', 'is_published']
