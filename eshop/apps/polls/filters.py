import django_filters

from django_filters.rest_framework import FilterSet


from apps.polls.models import Question



class QuestionFilter(FilterSet):

    question_text = django_filters.CharFilter(field_name="question_text", lookup_expr='icontains')
    
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date', 'is_sold']

