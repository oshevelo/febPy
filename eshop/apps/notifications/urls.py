from django.urls import path

from apps.notifications import views

app_name = 'notifications'

urlpatterns = [
    path('', views.NotificationList.as_view(), name='list'),
    path('<int:notification_id>/', views.NotificationDetail.as_view(), name='details'), 
]
