from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    SENDMETHODS = (
        ('email', 'email'),
        ('telegram', 'telegram'),
        ('viber', 'viber'),
        ('sms', 'sms'),
    )

    recipient = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)
    send_method = models.CharField(choices=SENDMETHODS, max_length=20)
    subject = models.CharField(max_length=200)


# Create your models here.
