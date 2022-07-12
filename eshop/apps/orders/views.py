
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import serializers
from .models import Order, OrderItem
from .serializers import OrderListSerializer, OrderDetailSerializer,  OrderItemDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer

    def get_object(self):
        return get_object_or_404(Order, pk=self.kwargs.get('order_id'), user=self.request.user)


class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemDetailSerializer

    def get_object(self):
        return get_object_or_404(OrderItem, pk=self.kwargs.get('order_item_id'), order__user=self.request.user)





