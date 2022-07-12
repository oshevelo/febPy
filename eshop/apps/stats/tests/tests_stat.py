from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .test_user import user_kw #using user from another modul
from apps.stats.models import UserAction

from django.utils import timezone


class UserActionTest(TestCase):
    def setUp(self):
        self.c = APIClient()

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
        new_user_action = UserAction.objects.create(data='', pub_date=timezone.now())
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
                    "id": new_user_action.id,
                    'data': "",
                    "pub_date": new_user_action.pub_date
                }
            ]
        })


