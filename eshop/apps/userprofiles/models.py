# from django.contrib.postgres.fields import ArrayField
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib import admin
from django.dispatch import receiver
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User

import uuid

from eshop.settings import TOKEN_TTL, PROJECT_BASE_URL


class UserProfile(models.Model):

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
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user'
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

    class Meta:
        ordering = ['user']

    @admin.display(description='Full name', ordering='user')
    def full_name(self):
        return self.user.get_full_name()

    @admin.display(description='E-mail', ordering='user')
    def main_email(self):
        return self.user.email


def create_activation_token():
    return uuid.uuid4()


class OneTimeToken(models.Model):
    token = models.CharField(primary_key=True, max_length=150, default=create_activation_token)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='token_bearer'
    )
    date_of_expiry = models.DateField()

    def send_activation_link(self):
        print(f'Sent to email={self.user.email}, link={PROJECT_BASE_URL}activate/?token={self.token}')


@receiver(post_save, sender=User)
def create_user_profile(sender, created, **kwargs):
    if created:
        user = kwargs.get('instance')
        up = UserProfile.objects.create(user=user,
                         date_of_birth=timezone.now()
                         )

        if not user.is_active:
            ott = OneTimeToken.objects.create(user=user,
                                              date_of_expiry=timezone.now()+TOKEN_TTL
                                              )
            ott.send_activation_link()
