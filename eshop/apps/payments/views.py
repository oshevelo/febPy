from django.http import HttpResponse
from rest_framework.response import Response

from .models import Payment, PaymentSystemLog
from .serializers import PaymentListSerializer, PaymentSystemLogSerializer
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from django.contrib.auth.models import User



def index(request):
    return HttpResponse('Hello on the Payment app')


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [IsAuthenticated]


class PaymentSystemLogList(generics.ListAPIView):
    queryset = PaymentSystemLog.objects.all()
    serializer_class = PaymentSystemLogSerializer
    pagination_class = pagination.LimitOffsetPagination

