from .models import UserAction
from .serializers import UserActionSerializer
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from .filters import UserActionFilter


class UserLastTenActionList(generics.ListCreateAPIView):
    queryset = UserAction.objects.order_by('data__action')[:10] #return only current user actions from 0 to 10
    serializer_class = UserActionSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_class = UserActionFilter
    permission_classes = [IsAuthenticated]












