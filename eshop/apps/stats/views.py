from .models import UserAction
from .serializers import UserActionSerializer
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from .filters import UserActionFilter


class UserActionList(generics.ListCreateAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_class = UserActionFilter
    permission_classes = [IsAuthenticated]











