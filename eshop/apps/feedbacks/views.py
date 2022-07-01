from rest_framework import generics, permissions
from apps.feedbacks.models import Feedback
from apps.feedbacks.paginations import FeedbackPagination
from apps.feedbacks.permissions import IsOwnerOrReadOnly
from apps.feedbacks.serializers import FeedbackSerializer, FeedbackDetailSerializer
from apps.feedbacks.filters import FeedbackFilter


class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    pagination_class = FeedbackPagination
    filterset_class = FeedbackFilter
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
