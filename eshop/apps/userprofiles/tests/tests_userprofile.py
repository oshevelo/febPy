from datetime import time, date

import rest_framework.settings
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from apps.userprofiles.models import UserProfile

user_kw = dict(
    username='admin',
    password='111',
    email='admin' + '@gmail.com',
)

user_kw['password'] = make_password(user_kw['password'])

test_profile_correct = {'username': 'admin',
                        'first_name': 'First',
                        'last_name': 'Last',
                        'date_of_birth': '1990-11-11',
                        'sex': 'MALE',
                        'preferable_language': 'UA',
                        'addresses_of_delivery': ['address1', 'address2'],
                        'telephones': ['1234-5678', '5432-1256'],
                        'additional_emails': ['admin@gmail.com', 'admin2@meta.ua']
                        }

test_profile_incorrect = {'username': 'admin',
                          'first_name': 'First',
                          'last_name': 'Last',
                          'date_of_birth': '90-11-11',
                          'sex': 'MALE',
                          'preferable_language': 'UA',
                          'addresses_of_delivery': ['address1', 'address2'],
                          'telephones': ['1234-5678', '5432-1256'],
                          'additional_emails': ['admingmail.com', 'admin2meta.ua']
                          }


def get_datetime_format(value):
    if value.lower() == 'iso-8601':
        return '%Y-%m-%d'
    else:
        return value


class UserProfileTest(TestCase):
    def setUp(self):
        self.c = APIClient()
        self.user = User.objects.create(**user_kw)

    def test_user_profile_created(self):
        self.c.login(username=self.user.username, password='111')
        response = self.c.get('/api/userprofile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'username': 'admin',
                          'first_name': '',
                          'last_name': '',
                          'date_of_birth': UserProfile.objects.get(user_id=self.user.id).date_of_birth. \
                                           strftime(get_datetime_format(rest_framework.settings.api_settings.DATETIME_FORMAT)),
                          'sex': 'OTHER',
                          'preferable_language': 'EN',
                          'addresses_of_delivery': None,
                          'telephones': None,
                          'additional_emails': None}
                         )

    def test_user_profile_update_success(self):
        self.c.login(username=self.user.username, password='111')
        response = self.c.put(
            path='/api/userprofile/',
            data=test_profile_correct,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, test_profile_correct)

    def test_user_profile_update_failed(self):
        self.c.login(username=self.user.username, password='111')
        response = self.c.put(
            path='/api/userprofile/',
            data=test_profile_incorrect,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'date_of_birth': ['Date has wrong format. Use one of these formats instead: '
                                                           'YYYY-MM-DD.'],
                                         'additional_emails': {0: ['Enter a valid email address.'], 1: ['Enter a '
                                                                                                        'valid email '
                                                                                                        'address.']}})

    def test_user_profile_delete_failed(self):
        self.c.login(username=self.user.username, password='111')
        response = self.c.delete(
            path='/api/userprofile/'
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
