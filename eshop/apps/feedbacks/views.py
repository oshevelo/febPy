from rest_framework import generics, permissions
from apps.feedbacks.models import Feedback
from apps.feedbacks.paginations import FeedbackPagination
from apps.feedbacks.serializers import FeedbackSerializer, FeedbackDetailSerializer


class FeedbackList(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    pagination_class = FeedbackPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Feedback.objects.filter(user_name=user, is_deleted=False)

    def perform_create(self, serializer):
        serializer.save(user_name=self.request.user)


class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Feedback.objects.filter(user_name=user, is_deleted=False)
