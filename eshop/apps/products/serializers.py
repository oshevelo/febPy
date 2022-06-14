from rest_framework import serializers
from .models import Product, Comments, Category

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price',]
        # add 'image.small', 'amnt_in_stock_status'

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'price', 'description',]
    # add 'amnt_in_stock_status', 'image.big', num_of_comments, delivery-method, payment_method, buy_button

class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['product', 'user', 'product_rating', 'pub_date']

class CommentsDetailsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['product', 'user', 'text', 'product_rating', 'pub_date']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'parent_category']

class CategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'parent_category']