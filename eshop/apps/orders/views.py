from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Order, OrderItem
from .serializers import OrderListSerializer, OrderDetailSerializer, OrderItemListSerializer, OrderItemDetailSerializer, OrderItemNestedSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
#from .paginations


def index(request):
    return HttpResponse("Hello")


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all() #rabotaet so spiskom
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

#do we need to add this function to filter user to see orders// show orders that are urs?
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer

    def get_object(self):
        print(self.kwargs)
        return get_object_or_404(Order, pk=self.kwargs.get('order_id'), user=self.request.user)


class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user)

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemDetailSerializer

    def get_object(self):
        print(self.kwargs)
        return get_object_or_404(OrderItem, pk=self.kwargs.get('order_item_id'))