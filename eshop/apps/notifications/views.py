import logging

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationSerializer, NotificationDetailSerializer 


logger = logging.getLogger(__name__)


class NotificationList(generics.ListCreateAPIView):
    
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = NotificationDetailSerializer
    
    

    def get_object(self):
        return get_object_or_404(Notification, pk=self.kwargs.get('notification_id'),recipient=self.request.user)
        

# Create your views here.
