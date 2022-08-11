from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductList.as_view(), name = 'ProductList'),
    path('product/<int:product_id>/', views.ProductDetails.as_view(), name = 'ProductDetails'),
    path('product/<int:product_id>/comments/', views.CommentsList.as_view(), name='CommentsList'),
    path('product/<int:product_id>/comments/<int:comments_id>/', views.CommentsDetails.as_view(), name='CommentsDetails'),
    path('category/', views.CategoryList.as_view(), name='CategoryList'),
    path('category/<int:category_id>/', views.CategoryDetails.as_view(), name='CategoryDetails'),
]