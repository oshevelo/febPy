from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartList.as_view(), name='cart-list'),
    path('<int:cart_id>', views.CartDetails.as_view(), name='cart-details'),
    path('<int:cart_id>/cartitem', views.CartItemList.as_view(), name='cartitem-list'),
    path('<int:cart_id>/cartitem/<int:cart_items_id>', views.CartItemDetails.as_view(), name='cartitem-details'),
]
