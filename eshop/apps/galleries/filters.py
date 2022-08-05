import django_filters
from django_filters.rest_framework import FilterSet

from apps.galleries.models import Image


class ImageFilter(FilterSet):
    class Meta:
        model = Image
        fields = ['upload', 'size']

