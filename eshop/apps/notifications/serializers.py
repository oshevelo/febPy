from django.contrib.auth.models import User	
from rest_framework import serializers
from apps.notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ['recipient', 'message_text', 'send_method','subject','source']
        
class NotificationDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ['recipient', 'message_text', 'send_method','subject','source']
        
        

