from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    SendMethods = (
        ('email', 'email'),
        ('telegram', 'telegram'),
        ('viber', 'viber'),
        ('sms', 'sms'),
    )

    User_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    MessageText = models.CharField(max_length=200)
    TimeStamp = models.DateTimeField(auto_now_add=True)
    SendMethod = models.CharField(choices=SendMethods, max_length=20)
    EventName = models.CharField(max_length=200)

# Create your models here.
