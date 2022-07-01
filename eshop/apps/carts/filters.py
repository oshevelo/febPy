from django_filters import rest_framework as filters

from apps.carts.models import Cart, CartItem


class CartFilter(filters.FilterSet):
    total_price = filters.BaseRangeFilter(field_name='total_price')

    class Meta:
        model = Cart
        fields = ['user', 'cart_items', 'total_price']


class CartItemFilter(filters.FilterSet):
    product_name = filters.CharFilter(field_name='product__name', lookup_expr='icontains')
    product_price = filters.BaseRangeFilter(field_name='product__price')

    class Meta:
        model = CartItem
        fields = ['product_name', 'product_price']
