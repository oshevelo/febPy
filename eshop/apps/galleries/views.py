from django.http import HttpResponse
from rest_framework.generics import get_object_or_404
from .models import Image
from .serializers import ImageListSerializer
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrPutOnly
from django.db.models import Q


def Index(request):
    return HttpResponse('Page for Image')

class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer
    pagination_class = pagination.LimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Image.objects.all()
        return Image.objects.filter(Q(owner=self.request.user) | Q(editor=self.request.user))


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageListSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrPutOnly]

    def get_object(self):
        if self.request.user.is_superuser:
            return get_object_or_404(Image, pk=self.kwargs.get('image_id'))
        return get_object_or_404(Image, Q(pk=self.kwargs.get('image_id')) & (Q(owner=self.request.user) | Q(editor=self.request.user)))


class ImageCreate(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer

