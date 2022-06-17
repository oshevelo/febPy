import django_filters
from django_filters.rest_framework import FilterSet
from .models import PointCount,Discount,Rating

class PointCountFilter(FilterSet):
    points__gt = django_filters.NumberFilter(field_name='count',lookup_expr='gt')
    points__lt = django_filters.NumberFilter(field_name='points',lookup_expr='lt')
    username = django_filters.CharFilter(field_name='user',lookup_expr='icontains')
    class Meta:
        model = PointCount
        fields = ['user','points__gt','points__lt']

#class DiscountFilter(FilterSet)

#class RatingFilter()