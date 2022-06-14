from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Comments, Category
from .serializers import ProductListSerializer, ProductDetailsSerializer, CommentsListSerializer, \
    CommentsDetailsSerilizer, CategoryListSerializer, CategoryDetailsSerializer
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
    queryset = Comments.objects.all()
    serializer_class = CommentsListSerializer

class CommentsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsDetailsSerilizer

    def get_object(self):
        return get_object_or_404(Comments, pk=self.kwargs.get('comments_id'))

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailsSerializer

    def get_object(self):
        return get_object_or_404(Category, pk=self.kwargs.get('category_id'))