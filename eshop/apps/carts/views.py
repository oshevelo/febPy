from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer, CartItemSerializer
from .models import Cart, CartItem
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from .paginations import CartPagination, CartItemPagination
from .filters import CartFilter, CartItemFilter


class CartList(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    pagination = CartPagination
    filterset_class = CartFilter

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Cart, pk=self.kwargs.get('cart_id'), user=self.request.user)


class CartItemList(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    pagination = CartItemPagination
    filterset_class = CartItemFilter

    def get_queryset(self):
        cart = get_object_or_404(Cart, pk=self.kwargs.get('cart_id'), user=self.request.user)
        return cart.cart_items.all()


class CartItemDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(CartItem, pk=self.kwargs.get('cart_items_id'))

