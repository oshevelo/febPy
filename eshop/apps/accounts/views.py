from django.shortcuts import render
# Create your views here.
from .serializers import DiscountListSerializer,DiscountModelSerializer,PointCountListSerializer,PointCountModelSerializer,RatingListSerializer,RatingModelSerializer
#from .rest
from django.shortcuts import get_object_or_404
from rest_framework import generics
#class DiscountModelView()
class DiscountList(generics.ListCreateAPIView):
    queryset = DiscountModelSerializer.objects.all()
    serializer_class=DiscountModelSerializer

class PointCountList(generics.ListCreateAPIView):
    queryset = PointCountModelSerializer.objects.all()
    serializer_class=DiscountModelSerializer

class RatingList(generics.ListCreateAPIView):
    queryset = RatingModelSerializer.objects.all()
    serializer_class=RatingModelSerializer


class RatingInstance(generics.ListCreateAPIView):
    serializer_class=RatingModelSerializer


class DiscountInstance(generics.ListCreateAPIView):
    serializer_class = DiscountModelSerializer

class PointCountInstance(generics.ListCreateAPIView):
    serializer_class = PointCountModelSerializer
    def get_object(self):
        return get_object_or_404(PointCount,)