# from django.contrib.postgres.fields import ArrayField
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib import admin
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfiles(models.Model):

    UKRAINIAN = 'UA'
    ENGLISH = 'EN'
    LANGUAGE_CHOICES = [
        (UKRAINIAN, 'Украинский'),
        (ENGLISH, 'English')
    ]

    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'
    SEX = [
        (MALE, _('Male')),
        (FEMALE, _('Female')),
        (OTHER, _('Other')),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        # default=1,
    )

    date_of_birth = models.DateField()
    sex = models.CharField(
        max_length=10,
        choices=SEX,
        default=OTHER,
    )

    preferable_language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default=ENGLISH)
    addresses_of_delivery = ArrayField(models.CharField(max_length=150), null=True, blank=True)
    telephones = ArrayField(models.CharField(max_length=16), null=True, blank=True)
    additional_emails = ArrayField(models.EmailField(max_length=150), null=True, blank=True)

    @admin.display(description='Full name', ordering='user')
    def full_name(self):
        return self.user.get_full_name()

    @admin.display(description='E-mail', ordering='user')
    def main_email(self):
        return self.user.email


def create_user_profile(sender, **kwargs):
    if sender is User:
        # print(f'kwargs = {kwargs}')
        up = UserProfiles(user=kwargs.get('instance'),
                          date_of_birth=timezone.now()
                          )
        up.save()


post_save.connect(create_user_profile)
