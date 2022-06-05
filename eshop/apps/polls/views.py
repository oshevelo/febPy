from django.http import HttpResponse
from .models import Question, Choice
from .serializers import QuestionListSerializer, QuestionDetailsSerializer
from .filters import QuestionFilter
from django.shortcuts import get_object_or_404
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    

def index2(request):
    return HttpResponse("index2index2index2index2index2Hello, world. You're at the polls index.")
    

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    pagination_class = pagination.LimitOffsetPagination
    filterset_class = QuestionFilter
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
    
        result = Question.objects.all()
        if self.request.user.is_superuser:
            return result
        return result.filter(author=self.request.user)
    

class QuestionOList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    permission_classes = []
#    pagination_class = pagination.LimitOffsetPagination

    
class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailsSerializer
    
    def get_object(self):
        if self.request.user.is_superuser:
            return get_object_or_404(Question, Q(pk=self.kwargs.get('question_id')))
        return get_object_or_404(Question, Q(pk=self.kwargs.get('question_id')) & (Q(author=self.request.user) | Q(editor=self.request.user)))
    
