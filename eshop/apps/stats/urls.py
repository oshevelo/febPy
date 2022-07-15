from django.urls import path

from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.UserLastTenActionList.as_view()),
]
