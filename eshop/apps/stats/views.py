from .models import UserAction
from .serializers import UserActionSerializer
from rest_framework import generics


class UserActionList(generics.ListCreateAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer










