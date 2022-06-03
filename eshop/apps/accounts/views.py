from django.shortcuts import render
# Create your views here.

from django.db.models import Q
from .serializers import DiscountModelSerializer,RatingModelSerializer, PointCountModelSerializer
#from .rest
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics


#class DiscountModelView()
class DiscountList(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class=DiscountModelSerializer
    def get_queryset(self):
        if self.request.user.is_superuser():
            return Discount.objects.all()
        else:
            return Discount.objects.filter(Q(Discount.user==self.request.user))


class PointCountList(generics.ListCreateAPIView):
    queryset = PointCount.objects.all()
    serializer_class=PointCountModelSerializer

#class RatingList(generics.ListCreateAPIView):
 #   queryset = Rating.objects.all()
  #  serializer_class=RatingModelSerializer


#class RatingInstance(generics.ListCreateAPIView):
 #   serializer_class=RatingModelSerializer


#class DiscountInstance(generics.ListCreateAPIView):
 #   serializer_class = DiscountModelSerializer

#class PointCountInstance(generics.ListCreateAPIView):
 #   serializer_class = PointCountModelSerializer
  #  permission_classes=[]
    #def get_object(self):
     #   return get_object_or_404(PointCount,)
