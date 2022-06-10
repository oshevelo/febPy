from django.urls import path, include


urlpatterns = [
    path('polls/',
        include('apps.polls.urls')),
    path('userprofile/',
        include('apps.userprofiles.urls')),
 ]
