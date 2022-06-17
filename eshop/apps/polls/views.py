from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import serializers
from .models import Question, Choice
from .serializers import QuestionListSerializer, QuestionDetailsSerializer, ChoiceListSerializer
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
    

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceListSerializer
    permission_classes = []


class ChoiceDetails(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ChoiceListSerializer
    permission_classes = []
    def get_object(self):
        return get_object_or_404(Choice, Q(pk=self.kwargs.get('choice_id')))


    
class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailsSerializer
    
    def get_object(self):
        if self.request.user.is_superuser:
            return get_object_or_404(Question, Q(pk=self.kwargs.get('question_id')))
        return get_object_or_404(Question, Q(pk=self.kwargs.get('question_id')) & (Q(author=self.request.user) | Q(editor=self.request.user)))

    def delete(self, *args, **kwargs):
        if self.get_object().length == 2:
            return Response({'error': "you shall not pass"}, status=400)
        return super().delete(self, *args, **kwargs)
        
        
        
    
