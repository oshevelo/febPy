from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('asdasadaasdx/', views.index2, name='index'),
    #path('question/', views.QuestionList.as_view(), name='QuestionList'),
    #path("discount/",views.DiscountView.as_view(),name='View Details'),
    #path("discount/", views.DiscountViewList.as_view(), name='View List'),
    #path("pont_coun/", views.DiscountView.as_view(), name='View Details'),

    #path('questiono/', views.QuestionOList.as_view(), name='QuestionList'),
    #path('question/<int:question_id>/', views.QuestionDetails.as_view(), name='QuestionDetails'),
    #path('discount/',views.)
]
