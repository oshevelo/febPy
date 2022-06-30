import django_filters
from django_filters.rest_framework import FilterSet
from .models import PointCount,Discount,Rating

class PointCountFilter(FilterSet):
    points_gt = django_filters.NumberFilter(field_name='points',lookup_expr='gt')
    points_lt = django_filters.NumberFilter(field_name='points',lookup_expr='lt')
    username = django_filters.CharFilter(field_name='user__username',lookup_expr='icontains')

    class Meta:
        model = PointCount
        fields = ['username','points_gt','points_lt']

class DiscountFilter(FilterSet):
    discount_gt = django_filters.NumberFilter(field_name='discount',lookup_expr='gt')
    discount_lt = django_filters.NumberFilter(field_name='discount', lookup_expr='lt')
    prev_count_gt = django_filters.NumberFilter(field_name='prev_count', lookup_expr='gt')
    prev_count_lt = django_filters.NumberFilter(field_name='prev_count', lookup_expr='lt')
    username = django_filters.CharFilter(field_name='user__username',lookup_expr='icontains')
    pointcount_gt = django_filters.NumberFilter(field_name='pointcount__points', lookup_expr='gt')
    pointcount_lt = django_filters.NumberFilter(field_name='pointcount__points', lookup_expr='lt')

    class Meta:
        model = Discount
        fields = ['username','discount_gt','discount_lt','prev_count_gt','prev_count_lt',]

class RatingFilter(FilterSet):
    percentile_gt = django_filters.NumberFilter(field_name='percentile',lookup_expr='gt')
    percentile_lt = django_filters.NumberFilter(field_name='percentile',lookup_expr='lt')
    username = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    pointcount_gt = django_filters.NumberFilter(field_name='pointcount__points', lookup_expr='gt')
    pointcount_lt = django_filters.NumberFilter(field_name='pointcount__points', lookup_expr='lt')

    class Meta:
        model = Rating
        fields = ['percentile_gt','percentile_lt','username',
                  'pointcount_gt',
                  'pointcount_lt',]
