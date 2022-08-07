from django.db import models
# the related_name specifies the name of the reverse relation from the USER model back to your model

# Create your models here.

from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from apps.shipments.models import Shipments
from apps.products.models import Product
from django.contrib import admin


class Order(models.Model):
    #order_items = None
    NEW = 'New'
    PAID = 'Paid'
    DELIVERED = 'Delivered'
    CANCELED = 'Canceled'
    COMPLETED = 'Completed'

    ORDER_TYPE = [
        ('NEW', 'New'),
        ('PAID', 'Paid'),
        ('DELIVERED', 'Delivered'),
        ('CANCELED', 'Canceled'),
        ('COMPLETED', 'Completed'),
    ]

    order_type = models.CharField(max_length=20, choices=ORDER_TYPE, default=NEW)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Customer')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Last updated')
    shipment = models.ForeignKey(Shipments, on_delete=models.CASCADE, related_name='orders')
    amount_to_pay = models.DecimalField(max_digits=20, decimal_places=2)

    @property
    def amount_to_pay(self):
        return sum([item.product.price * item.quantity for item in self.order_items.all()]) # ili self.items.all()

    @property
    def shipment_address(self):
        return f'{self.shipment.delivery_company}, {self.shipment.delivery_office_number}, {self.shipment.addressee_last_name}, {self.shipment.addressee_phone}'

    def __str__(self):
        return f'{self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def price(self):
        return f'{self.product.price}'

    def __str__(self):
        return f"{self.id}"
