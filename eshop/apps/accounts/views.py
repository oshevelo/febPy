from django.db.models import Q
from .serializers import DiscountModelSerializer, RatingModelSerializer, PointCountModelSerializer
from .filters import PointCountFilter, DiscountFilter, RatingFilter
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUserOrSafeOnly


# class DiscountModelView()
class DiscountList(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountModelSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrSafeOnly]
    filterset_class = DiscountFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Discount.objects.all()
        else:
            return Discount.objects.filter(Q(user=self.request.user))


class DiscountDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountModelSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrSafeOnly]

    def get_object(self):
        obj = get_object_or_404(Discount, pk=self.kwargs.get("discount_id"))
        self.check_object_permissions(self.request, obj)
        return obj


class PointCountList(generics.ListCreateAPIView):
    # queryset = PointCount.objects.all()
    serializer_class = PointCountModelSerializer
    filterset_class = PointCountFilter
    permission_classes = [IsAuthenticated, IsSuperUserOrSafeOnly]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return PointCount.objects.all()
        else:
            return PointCount.objects.filter(Q(user=self.request.user))


class PointCountDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PointCountModelSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrSafeOnly]

    def get_object(self):
        # if self.request.user.is_superuser:
        #     return get_object_or_404(PointCount, pk=self.kwargs.get("pointcount_id"))
        # return get_object_or_404(PointCount, Q(pk=self.kwargs.get('pointcount_id')) & Q(user=self.request.user))
        obj = get_object_or_404(PointCount, pk=self.kwargs.get("pointcount_id"))
        self.check_object_permissions(self.request, obj)
        return obj


class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer
    permission_classes = [IsSuperUserOrSafeOnly]
    filterset_class = RatingFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Rating.objects.all()
        return Rating.objects.filter(Q(user=self.request.user))


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingModelSerializer
    permission_classes = [IsAuthenticated, IsSuperUserOrSafeOnly]

    def get_object(self):
        obj = get_object_or_404(Rating, pk=self.kwargs.get("rating_id"))
        self.check_object_permissions(self.request, obj)
        return obj
