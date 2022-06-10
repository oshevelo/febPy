from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from apps.stats.models import UserAction

from django.utils import timezone


class UserActionTest(TestCase):
    def setUp(self) -> None:
        self.c = APIClient()
        user_kw = dict(
            username='admin',
            password='111',
            email='admin' + '@gmail.com',
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)

    def test_list_check_permission(self):
        response = self.c.get('/stat/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_empty(self):
        self.c.login(username=self.user.username, password='111')
        response = self.c.get('/stat/')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        })

    def test_list_no_empty(self):
        new_user_action = UserAction.objects.create(user=User.objects.get(username='admin'), data='', pub_date=timezone.now())
        self.c.login(username=self.user.username, password='111')
        response = self.c.get('/stat/')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "user": "admin",
                    'data': "",
                    "pub_date": timezone.now()
                }
            ]
        })


