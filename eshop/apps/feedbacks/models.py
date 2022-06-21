from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps_generic.whodidit.models import WhoDidIt


class Feedback(WhoDidIt):
    ORDER_PROBLEM = 'OP'
    DELIVERY_PROBLEM = 'DP'
    SOME_QUESTION = 'SQ'
    SOME_PROBLEM = 'SM'

    SUBJECT = [
        (ORDER_PROBLEM, 'Problem with order'),
        (DELIVERY_PROBLEM, 'Problem with delivery'),
        (SOME_QUESTION, 'Some question'),
        (SOME_PROBLEM, 'Some problem'),
    ]

    user = models.ForeignKey(User, related_name='feedbacks', verbose_name='User name', on_delete=models.PROTECT)
    user_phone = PhoneNumberField(blank=True, null=True, verbose_name='User phone number')
    subject = models.CharField(max_length=2, choices=SUBJECT, default=SOME_QUESTION)
    feedback = models.TextField(max_length=1024, blank=False, verbose_name='Feedback text')
    is_published = models.BooleanField(default=False, verbose_name='Published')

    def __str__(self):
        return f'{self.subject}/{self.user.username}'

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ['created_on']
