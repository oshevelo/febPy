from rest_framework import pagination


class CartPagination(pagination.LimitOffsetPagination):
    default_limit = 5
    max_limit = 50


class CartItemPagination(pagination.LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
