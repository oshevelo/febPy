from django.http import HttpResponse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Payment, PaymentSystemLog
from .serializers import PaymentListSerializer, PaymentSystemLogSerializer
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from django.contrib.auth.models import User
from .permissions import IsOwnerOrPutOnly
from django.db.models import Q


def Index(request):
    return HttpResponse('Hello on Payment side')


class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Payment.objects.all()
        return Payment.objects.filter(Q(owner=self.request.user) | Q(editor=self.request.user))


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentListSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrPutOnly]

    def get_object(self):
        if self.request.user.is_superuser:
            return get_object_or_404(Payment, pk=self.kwargs.get('payment_id'))
        return get_object_or_404(Payment, Q(pk=self.kwargs.get('payment_id')) & (Q(owner=self.request.user) | Q(editor=self.request.user)))


class PaymentCreate(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer


# class PaymentSystemLogList(generics.ListAPIView):
#     queryset = PaymentSystemLog
#     serializer_class = PaymentSystemLogSerializer
#     pagination_class = pagination.LimitOffsetPagination
#     permission_classes = [IsAuthenticated]








