from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=20000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return f'product {self.name}, sku {self.sku}'


class Comments(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=20000)
    product_rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)])
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.text} published by {self.user} on {self.pub_date}'

class Category(Product):
    category_name = models.CharField(max_length=200)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name

