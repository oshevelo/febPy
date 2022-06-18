from django.urls import path

from .import views

app_name = 'accounts'

urlpatterns = [
    path('pointcount', views.PointCountList.as_view(), name='list'),
    path('pointcount/<int:pointcount_id>/', views.PointCountDetails.as_view(), name='details'),

    path('discount/', views.DiscountList.as_view(), name='list'),
    path('discount/<int:discount_id>/', views.DiscountDetails.as_view(), name='details'),

    path('rating/', views.RatingList.as_view(), name='list'),
    path('rating/<int:rating_id>/', views.RatingDetail.as_view(), name='details'),

]