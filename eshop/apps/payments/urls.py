# from django.urls import path
#
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('payment/', views.PaymentList.as_view(), name='PaymentList'),
#     path('paymentlog/', views.PaymentSystemLogList.as_view(), name='PaymentLogList')
#
# ]

from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('pay/', views.PaymentList.as_view(), name='PaymentList'),
    path('log/', views.PaymentSystemLogList.as_view(), name='PaymentLogList'),

]
