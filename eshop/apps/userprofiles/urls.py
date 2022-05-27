from django.urls import path

from . import views

urlpatterns = [
    # path('', views.UserProfileList.as_view()),
    # path('<int:pk>/', views.UserProfileDetail.as_view()),
    path('signup/', views.UserCreate.as_view()),
    path('', views.UserProfileDetail.as_view()),

]