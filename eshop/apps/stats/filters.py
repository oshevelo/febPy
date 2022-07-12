import django_filters

from django_filters.rest_framework import FilterSet

from .models import UserAction


class UserActionFilter(FilterSet):
    user = django_filters.CharFilter(field_name="user__email", lookup_expr='icontains')

    class Meta:
        model = UserAction
        fields = ['pub_date', 'user']
