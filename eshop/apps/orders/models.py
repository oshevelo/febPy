from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from apps.shipments.models import Shipments
from apps.products.models import Product


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

    created = models.DateTimeField(default=datetime.datetime)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE, default=NEW)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Customer')
    value = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[validate_order_value]
    )
    shipment = models.ForeignKey(Shipments, on_delete=models.CASCADE, related_name='Delivery_Address')

    @property
    def delivery_address(self):
        return f' {self.shipment.delivery_company}, {self.shipment.delivery_office_number}, {self.shipment.addressee_last_name}'


    def __str__(self):
        return f'{self.user}, {self.created}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='Order', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.order}'
