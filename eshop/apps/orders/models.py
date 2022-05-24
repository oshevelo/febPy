from django.db import models

# Create your models here.

from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
import django.contrib.auth
#from product.models import Product



class ShippingAddress(models.Model):
    # name of the recipient
    name = models.CharField('Full name', max_length=512, default=False)
    address_line = models.CharField('Address line', max_length=1024, default=False)
    post_code = models.CharField('Postcode', max_length=8, default=False)
    city = models.CharField('City', max_length=56, default=False)
    country = models.CharField('Country', max_length=56, default=False)

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

    @property
    def order_value(self):
        return sum([Product.item.price * item.quantity for item in self.order_items.all()])

    def validate_order_value(order_value):
        if order_value <= 0:
            raise ValidationError('Total value of the order should be more than 0.')


    created = models.DateTimeField('Created')
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE, default=NEW)

    #orders can be placed without the user authenticating  -> do not need to have customer ID
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name="Customer")
    value = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[validate_order_value],
    )

    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, default=False)



    def __str__(self):
        return f'{self.user}, {self.created}'


class OrderItem(models.Model):
    #product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='order_item',  on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.order}'






