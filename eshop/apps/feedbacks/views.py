from rest_framework import generics, permissions
from apps.feedbacks.models import Feedback
from apps.feedbacks.paginations import FeedbackPagination
from apps.feedbacks.serializers import FeedbackSerializer, FeedbackDetailSerializer


class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.filter(is_deleted=False)
    serializer_class = FeedbackSerializer
    pagination_class = FeedbackPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
