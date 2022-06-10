from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartList.as_view(), name='CartList'),
    path('<int:cart_id>', views.CartDetails.as_view(), name='CartDetails'),
    path('<int:cart_id>/cartitem', views.CartItemList.as_view(), name='CartItemList'),
    path('<int:cart_id>/cartitem/<int:cart_items_id>', views.CartItemDetails.as_view(), name='CartItemDetails'),
]
