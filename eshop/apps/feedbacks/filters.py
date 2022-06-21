import django_filters
from django_filters.rest_framework import FilterSet

from apps.feedbacks.models import Feedback


class FeedbackFilter(FilterSet):
    feedback = django_filters.CharFilter(field_name='feedback', lookup_expr='icontains')

    class Meta:
        model = Feedback
        fields = ['subject', 'feedback', 'is_published']
