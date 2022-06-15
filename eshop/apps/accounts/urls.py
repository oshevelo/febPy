from django.urls import path

from .import views

app_name = 'accounts'

urlpatterns = [
    path('pointcount', views.PointCountList.as_view(), name='list'),
    path('pointcount/<int:notification_id>/', views.PointCountList.as_view(), name='details'),

    path('discount/', views.DiscountList.as_view(), name='list'),
    path('discount/<int:notification_id>/', views.DiscountList.as_view(), name='details'),

    path('rating/', views.RatingList.as_view(), name='list'),
    path('rating/<int:notification_id>/', views.DiscountList.as_view(), name='details'),

]