from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('asdasadaasdx/', views.index2, name='index'),
    path('question/', views.QuestionList.as_view(), name='QuestionList'),
    path('question/<int:question_id>/', views.QuestionDetails.as_view(), name='QuestionDetails'),
    path('choice/', views.ChoiceList.as_view(), name='ChoiceList'),
    path('choice/<int:choice_id>/', views.ChoiceDetails.as_view(), name='ChoiceDetails'),
]
