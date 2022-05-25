from django.core.exceptions import ValidationError
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

    PAYPAL = 'PayPal'
    LIQPAY = 'Liqpay'
    PORTMONE = 'Portmone'

    PAYMENT_SYSTEM_CHOICE = [
        (PAYPAL, 'PayPal'),
        (LIQPAY, 'Liqpay'),
        (PORTMONE, 'Portmone'),
    ]

    def validate_price(value):
        if value <= 0:
            raise ValidationError(
                'price must be higher then 0',
                params={'value': value},
            )

    # order = models.ForeignKey(Order, on_delete=models.PROTECT)

    payment_system = models.CharField(max_length=30, choices=PAYMENT_SYSTEM_CHOICE, default=PAYPAL)
    payment_status = models.CharField(max_length=15, choices=PAYMENT_STATUS_CHOICE, default=PROCESSING)
    products_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.0, validators=[validate_price])
    delivery_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.0, validators=[validate_price])

    @property
    def total_price(self):
        return self.products_price + self.delivery_price


class PaymentSystemLog(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT, default=None)
    request_data = models.TextField(blank=True, default=None)  # What Payment_system sent to us
    response_data = models.TextField(blank=True, default=None)  # What we got back from our request
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

