from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=20000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount_in_stock = models.IntegerField()

    def __str__(self):
        return self.name

class Сomments(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=20000)
    product_rating = models.CharField(max_length=5)
    pub_date = models.DateTimeField('date published')

class Category(Product):
    category_name = models.CharField(max_length=200)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE)

