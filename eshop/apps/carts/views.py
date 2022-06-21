from rest_framework.permissions import IsAuthenticated
from .serializers import CartListSerializer, CartItemListSerializer, CartDetailsSerializer, CartItemDetailsSerializer
from .models import Cart, CartItem
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from .paginations import CartPagination, CartItemPagination


class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    pagination = CartPagination

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartDetailsSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Cart, pk=self.kwargs.get('cart_id'), user=self.request.user)


class CartItemList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    pagination = CartItemPagination

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class CartItemDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemDetailsSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_object(self):
        return get_object_or_404(CartItem, pk=self.kwargs.get('cart_items_id'))

