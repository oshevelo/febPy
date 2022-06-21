from django.http import HttpResponse
from rest_condition import And, Or
from rest_framework.generics import get_object_or_404

from .models import Payment, PaymentSystemLog
from .permissions import IsEditable, IsOwnedBy
from .serializers import PaymentListSerializer, PaymentSystemLogSerializer
from .filters import PaymentFilter
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from api.permissions import RequestIsCreate, RequestIsDelete, RequestIsUpdate, RequestIsReadOnly


def Index(request):
    return HttpResponse('Hello on payment side')


class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filterset_class = PaymentFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Payment.objects.all()
        return Payment.objects.filter(Q(owner=self.request.user) | Q(editor=self.request.user))


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentListSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [IsAuthenticated,
                          Or(RequestIsReadOnly,
                              And(RequestIsUpdate, IsEditable),
                              And(RequestIsDelete, IsOwnedBy))]

    def get_object(self):
        if self.request.user.is_superuser:
            return get_object_or_404(Payment, pk=self.kwargs.get('payment_id'))
        return get_object_or_404(Payment, Q(pk=self.kwargs.get('payment_id')) & (Q(owner=self.request.user) | Q(editor=self.request.user)))


class PaymentCreate(generics.CreateAPIView):
    serializer_class = PaymentListSerializer
    permission_classes = [IsAuthenticated]


class PaymentSystemLogList(generics.ListCreateAPIView):
    queryset = PaymentSystemLog.objects.all()
    serializer_class = PaymentSystemLogSerializer
    permission_classes = [IsAuthenticated]
