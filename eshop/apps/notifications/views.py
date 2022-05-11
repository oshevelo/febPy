from django.shortcuts import render

class NotificationList(generics.ListCreateAPIView):
    NotificationSet = Notification.objects.all()
    #serializer_class = NotificationSerializer

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    
    #serializer_class = NotificationSerializer

    def get_object(self):
        obj = get_object_or_404(Notification, pk=self.kwargs.get('notification_id'))
        return obj

# Create your views here.
