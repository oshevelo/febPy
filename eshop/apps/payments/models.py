from django.db import models

# Create your models here.
# from eshop.apps.orders.models import Order


class Payment(models.Model):

    COMPLETED = 'Completed'
    CANCELED = 'Canceled'
    PROCESSING = 'Processing'

    PAYMENT_STATUS_CHOICE = [
        (COMPLETED, 'Completed'),
        (PROCESSING, 'Processing'),
        (CANCELED, 'Canceled'),
    ]
    # order = models.ForeignKey(Order, on_delete=models.PROTECT)
    payment_status = models.CharField(max_length=15, choices=PAYMENT_STATUS_CHOICE, default=PROCESSING)
    products_price = models.DecimalField(max_digits=9, decimal_places=2, default="0.0")
    delivery_price = models.DecimalField(max_digits=9, decimal_places=2, default="0.0")

    @property
    def total_price(self):
        return self.products_price + self.delivery_price if self.delivery_price else self.products_price


class PaymentSystemLog(models.Model):
    raw_data = models.TextField(blank=True)  # What Payment_system sent to us
    response = models.TextField(blank=True)  # What we got back from our request
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

