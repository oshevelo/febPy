import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_better_admin_arrayfield.models.fields import ArrayField


class ShopInfo(models.Model):

    city = models.CharField(max_length=85)
    address = models.CharField(max_length=150)
    location_longitude = models.DecimalField(max_digits=8, decimal_places=3)
    location_latitude = models.DecimalField(max_digits=8, decimal_places=3)
    phone_numbers = ArrayField(models.CharField(max_length=16), null=True, blank=True)
    emails = ArrayField(models.EmailField(max_length=150, null=True, blank=True))

    def __str__(self):
        return f"{self.city} - {self.address}"


class ShopDaySchedule(models.Model):
    DEFAULT_OPEN_TIME = datetime.time(hour=8)
    DEFAULT_CLOSE_TIME = datetime.time(hour=17)

    shop = models.ForeignKey(ShopInfo, on_delete=models.CASCADE)
    day = models.IntegerField(default=1, validators=[MaxValueValidator(7), MinValueValidator(1)])
    open_hour = models.TimeField(default=DEFAULT_OPEN_TIME)
    close_hour = models.TimeField(default=DEFAULT_CLOSE_TIME)
