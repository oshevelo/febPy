from django.shortcuts import render
from rest_framework import generics, permissions
from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationSerializer, NotificationDetailSerializer 


class NotificationList(generics.ListCreateAPIView):
    
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = NotificationDetailSerializer

    def get_object(self):
        obj = get_object_or_404(Notification, pk=self.kwargs.get('notification_id'))
        return obj

# Create your views here.
