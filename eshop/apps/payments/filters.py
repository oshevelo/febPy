import django_filters
from django_filters.rest_framework import FilterSet

from apps.payments.models import Payment


class PaymentFilter(FilterSet):
    class Meta:
        model = Payment
        fields = ['status', 'system']

