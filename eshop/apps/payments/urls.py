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
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'Payment', views.PaymentViewSet, basename='payment')
router.register(r'PaymentLog', views.PaymentLogViewSet, basename='paymentlog')
router.register(r'User', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),

]
