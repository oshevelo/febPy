from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.OrderList.as_view(), name='OrderList'),
    path('order/<int:order_id>/', views.OrderDetail.as_view(), name='OrderDetail'),
    path('order/<int:order_id>/<order_item>', views.OrderItemDetail.as_view(), name='OrderItemDetail'),
]
