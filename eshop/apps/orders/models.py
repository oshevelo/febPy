from django.db import models

# Create your models here.

from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
import django.contrib.auth #?? installed apps


class ShippingAddress(models.Model):
    name = models.CharField('Full name', max_length=512)  # imja polychatelia
    address_line1 = models.CharField('Address line 1', max_length=512)
    address_line2 = models.CharField('Address line 2', max_length=512)
    post_code = models.CharField('Postcode', max_length=8)
    city = models.CharField('City', max_length=56)
    country = models.CharField('Country', max_length=56)

    class Meta:
        verbose_name = "Shipping Address"

class Order(models.Model):

    NEW = 'New'
    PAID = 'Paid'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'

    ORDER_TYPE = [
        ('NEW', 'New'),
        ('PAID', 'Paid'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]

    created = models.DateTimeField('Created')
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE, default=NEW)

    #orders can be placed without the user authenticating  -> do not need to have customer ID
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE) #null-True, blank=True???


    def __str__(self):
        return self.order_type, self.primary_key


class OrderItem(models.Model):
    #product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True) #eshe nyjno napisat class Product
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def order_value(self):
        return sum([Product.item.price * item.quantity for item in self.order_items.all()])  # ??
    # question product item - kak pisat

        ## gde ety fynkciu pisat : v klase Orders ili OrderItem
    def validate_order_value(order_value):
        if order_value <= 0:
            raise ValidationError('Total price for the order should be more than 0')


