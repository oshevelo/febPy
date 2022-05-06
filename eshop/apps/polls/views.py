from django.http import HttpResponse
from .models import Question, Choice
from .serializers import QuestionListSerializer, QuestionDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    

def index2(request):
    return HttpResponse("index2index2index2index2index2Hello, world. You're at the polls index.")
    

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    

class QuestionOList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    permission_classes = []
#    pagination_class = pagination.LimitOffsetPagination

    
class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailsSerializer
    
    def get_object(self):
        #1/0
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))
    
