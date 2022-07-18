from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from ..models import PointCount, Rating, Discount



class RatingTest(TestCase):
    def setUp(self) -> None:
        self.c = APIClient()
        user_kw = dict(username='just_user', password='password', email='user@gmail.com')
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)

    def test_list_permissions(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get('/api/accounts/rating/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        print(response.data['results'][0]['user'], self.user.id)
        self.assertEqual(response.data['results'][0]['user'], self.user.id)

    def test_this_users_account_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/rating/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_users_pointcount_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/rating/{self.user.id-1}/', follow=True)
        print('response other user', response.status_code)
        print(self.user.id)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_object(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.delete(f'/api/accounts/rating/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.put(f'/api/accounts/rating/{self.user.id}/', {'percentile': 0.98}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
