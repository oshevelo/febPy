import logging

from django.db import models
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

class Notification(models.Model):

    EMAIL = 'email'
    TELEGRAM = 'telegram'
    VIBER = 'viber'
    SMS = 'sms'    
    
    
    CART = 'cart'
    CATALOG = 'catalog'
    DISCOUNT = 'discount'
    INFO = 'info'
    NOTIFICATIONS = 'notifications'
    ORDER = 'order'
    PAYMENT = 'payment'
    PRODUCT = 'product'
    SHIPMENT = 'shipment'
    USERPROFILE = 'user_profile'
    OTHERSOURCE = 'other_source'
    
    SENDMETHODS = (
        (EMAIL, 'email'),
        (TELEGRAM, 'telegram'),
        (VIBER, 'viber'),
        (SMS, 'sms'),
    )
     
    SOURCE = (
        (CART, 'cart'),
        (CATALOG, 'catalog'),
        (DISCOUNT, 'discount'),
        (INFO, 'info'),
        (NOTIFICATIONS, 'notifications'),
        (ORDER, 'order'),
        (PAYMENT, 'payment'),
        (PRODUCT, 'product'),
        (SHIPMENT, 'shipment'),
        (USERPROFILE, 'user_profile'),
        (OTHERSOURCE, 'other_source')
    )
 

    recipient = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)
    send_method = models.CharField(choices=SENDMETHODS, max_length=20)
    subject = models.CharField(max_length=200)
    source = models.CharField(max_length=200, choices=SOURCE,default=OTHERSOURCE)
    
    def __str__(self):
        return f"{self.source} {self.recipient} {self.subject} {self.time_stamp} {self.send_method}"
        
        


# Create your models here.
