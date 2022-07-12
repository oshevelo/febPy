from django.urls import path, include


urlpatterns = [
    path('orders/', include('apps.orders.urls')),
    path('polls/',
        include('apps.polls.urls')),
    path('userprofile/',
        include('apps.userprofiles.urls')),

    path('payment/',
         include('apps.payments.urls')),
    path('accounts/',include('apps.accounts.urls')),

    path('galleries/',
         include('apps.galleries.urls')),
    path('cart/',
         include('apps.carts.urls')),
    path('notifications/', 
        include('apps.notifications.urls')),
]

