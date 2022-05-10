from django.db import models

# Create your models here.

from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


class Orders(models.Model):
    order_id = models.IntegerField(max_length=12)
    #OR AND ?
    primary_key = True


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

    date_created = models.DateTimeFields('date created')
    order_type = models.Charfield(max_lengths=20, choices=ORDER_TYPE, default=NEW)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    item = models.ManyToManyField(Item, on_delete=models.CASCADE)

    def validate_order_value(order_value):
        if order_value <= 0:
            raise ValidationError('Total price for the order should be more than 0 UAH')


    def __str__(self):
        return self.order_type, self.primary_key






