from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.OrderList.as_view(), name='OrderList'),
    path('order/<int:order_id>/', views.OrderDetail.as_view(), name='OrderDetail'),
    path('orderitem/', views.OrderItemList.as_view(), name='OrderItemList'),
    path('orderitem/<int:orderitem_id>', views.OrderItemDetail.as_view(), name='OrderItemDetail'),
]
