from django.shortcuts import render
# Create your views here.
#from .filters import PointCountFilter
from django.db.models import Q
from .serializers import DiscountModelSerializer,RatingModelSerializer, PointCountModelSerializer
#from .rest
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .permissions import IsSuperUserOrSafeOnly

#class DiscountModelView()
class DiscountList(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class=DiscountModelSerializer
    permission_classes=[]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Discount.objects.all()
        else:
            return Discount.objects.filter(Q(user=self.request.user))


class DiscountDetails(generics.RetrieveDestroyAPIView):
    serializer_class=DiscountModelSerializer
    permission_classes=[IsSuperUserOrSafeOnly]

    def get_object(self):
        if self.request.user.is_superuser:
            return get_object_or_404(Discount,pk=self.kwargs.get("discount_id"))
        return get_object_or_404(Discount,Q(pk=self.kwargs.get('discount_id'))&Q(user=self.request.user))




class PointCountList(generics.ListCreateAPIView):
    queryset = PointCount.objects.all()
    serializer_class=PointCountModelSerializer
    permission_classes=[]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return PointCount.objects.all()
        else:
            return PointCount.objects.filter(Q(user=self.request.user))

    def get_object(self):
        if self.request.user.is_superuser:
            return get_object_or_404(PointCount,ok=self.kwargs.get("pointcount_id"))
        return get_object_or_404(Discount,Q(pk=self.kwargs.get('pointcount_id'))&Q(user=self.request.user))


class PointCountDetails(generics.RetrieveDestroyAPIView):
    serializer_class=PointCountModelSerializer
    permission_classes=[]

    def get_object(self):
        if self.request.user.is_superuser:
            return get_object_or_404(PointCount,pk=self.kwargs.get("pointcount_id"))
        return get_object_or_404(PointCount,Q(pk=self.kwargs.get('pointcount_id'))&Q(user=self.request.user))




class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class=RatingModelSerializer
    permission_classes=[IsSuperUserOrSafeOnly]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Rating.objects.all()
        return Rating.objects.filter(Q(user=self.request.user))


class RatingDetail(generics.RetrieveDestroyAPIView):
    serializer_class=RatingModelSerializer
    permission_classes=[IsSuperUserOrSafeOnly]

    def get_object(self):
        if self.request.user.is_superuser:
            return get_object_or_404(Rating,pk=self.kwargs.get("rating_id"))
        return get_object_or_404(Rating,Q(pk=self.kwargs.get('rating_id'))&Q(user=self.request.user))
