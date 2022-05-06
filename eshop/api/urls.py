from django.urls import path, include


urlpatterns = [
    path('polls/',
        include('apps.polls.urls')),
    #path('orders/',
    #    include('apps.orders.urls')),
]
