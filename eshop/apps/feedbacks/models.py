from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    ORDER_PROBLEM = 'OP'
    DELIVERY_PROBLEM = 'DP'
    SOME_QUESTION = 'SQ'
    SOME_PROBLEM = 'SM'

    FEEDBACK_SUBJECT = [
        (ORDER_PROBLEM, 'Problem with order'),
        (DELIVERY_PROBLEM, 'Problem with delivery'),
        (SOME_QUESTION, 'Some question'),
        (SOME_PROBLEM, 'Some problem'),
    ]

    user = models.ForeignKey(User, related_name='feedbacks', verbose_name='User name', on_delete=models.PROTECT)
    feedback_to = models.CharField(max_length=2, choices=FEEDBACK_SUBJECT, default=SOME_QUESTION)
    user_email = models.EmailField(null=True, blank=True, verbose_name='User email')
    user_phone = PhoneNumberField(blank=True, null=True, verbose_name='User phone number')
    feedback = models.TextField(max_length=1024, blank=False, verbose_name='Feedback text')
    is_published = models.BooleanField(default=False, verbose_name='Published')
    is_deleted = models.BooleanField(default=False, verbose_name='Deleted')
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, editable=False, verbose_name='Updated at')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ['created_at']
