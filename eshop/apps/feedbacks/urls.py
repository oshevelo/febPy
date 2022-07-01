from django.urls import path
from apps.feedbacks import views

app_name = 'feedbacks'

urlpatterns = [
    path('', views.FeedbackList.as_view(), name='feedback-list'),
    path('<int:pk>/', views.FeedbackDetail.as_view(), name='feedback-by-id'),
]
