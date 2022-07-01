from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Comments, Category
from .serializers import ProductListSerializer, ProductDetailsSerializer, CommentsListSerializer, \
    CommentsDetailsSerilizer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics

# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailsSerializer

    def get_object(self):
        return get_object_or_404(Product, pk=self.kwargs.get('product_id'))

class CommentsList(generics.ListCreateAPIView):
    # queryset = Comments.objects.all()
    serializer_class = CommentsListSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comments.objects.filter(product=self.request.product_id)

class CommentsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsDetailsSerilizer

    def get_object(self):
        return get_object_or_404(Comments, pk=self.kwargs.get('comments_id'))

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    def get_object(self):
        return get_object_or_404(Category, pk=self.kwargs.get('category_id'))