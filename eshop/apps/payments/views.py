from django.http import HttpResponse
from rest_framework.response import Response

from .models import Payment, PaymentSystemLog
from .serializers import PaymentListSerializer, PaymentSystemLogSerializer, UserSerializer
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from django.contrib.auth.models import User



# def index(request):
#     return HttpResponse('Hello on the Payment app')


# class PaymentList(generics.ListCreateAPIView):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentListSerializer
#     pagination_class = pagination.LimitOffsetPagination
#     permission_classes = [IsAuthenticated]
#
#
# class PaymentSystemLogList(generics.ListCreateAPIView):
#     queryset = PaymentSystemLog.objects.all()
#     serializer_class = PaymentSystemLogSerializer
#     pagination_class = pagination.LimitOffsetPagination


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer


class PaymentLogViewSet(viewsets.ModelViewSet):
    queryset = PaymentSystemLog.objects.all()
    serializer_class = PaymentSystemLogSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
