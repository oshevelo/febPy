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
    path('', views.Index),
    path('pay/', views.PaymentList.as_view(), name='PaymentList'),
    path('pay/<int:payment_id>/', views.PaymentDetail.as_view(), name='PaymentDetail'),
    path('pay/create/', views.PaymentCreate.as_view(), name='PaymentCreate'),
    path('log/', views.PaymentSystemLogList.as_view(), name='PaymentLogList'),

]
