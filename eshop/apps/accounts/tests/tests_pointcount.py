from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from ..models import PointCount, Rating, Discount
from django.urls import reverse


class PointCountTest(TestCase):
    def setUp(self) -> None:
        self.c = APIClient()
        user_kw = dict(username='just_user', password='password', email='user@gmail.com')
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.superuser = User.objects.create_superuser(username='admin', email='admin@test.com', password='password')

    def test_list_permissions(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get('/api/accounts/pointcount/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        print(response.data['results'][0]['user'], self.user.id)
        self.assertEqual(response.data['results'][0]['user'], self.user.id)

    def test_this_users_account_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/pointcount/{self.user.id}/')
        print(response.data)
        self.assertEqual(response.data, {'user': self.user.id, 'points': 0.0}
                         )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_users_pointcount_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/pointcount/3/', follow=True)
        print('response other user', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # конечно, здесь и будет возвращаться 404, потому что объекта с id=3 попросту нет. Т.е. это тест на
        # наличие объекта, а не на действие permissions

    def test_delete_object(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.delete(f'/api/accounts/pointcount/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.put(f'/api/accounts/pointcount/{self.user.id}/', {'points': 100}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # нужно попробовать такой же тест провести под суперюзером, чтобы убедиться, что суперюзер может делать PUT