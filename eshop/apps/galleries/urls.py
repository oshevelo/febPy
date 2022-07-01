from django.urls import path

from apps.galleries import views

app_name = 'galleries'

urlpatterns = [
    path('', views.Index),
#    path('admin/', imageadmin),
    path('galleries/', views.ImageList.as_view(), name='ImageList'),
    path('galleries/<int:image_id>/', views.ImageDetail.as_view(), name='ImageDetail'),
    path('galleries/create/', views.ImageCreate.as_view(), name='ImageCreate'),
]
