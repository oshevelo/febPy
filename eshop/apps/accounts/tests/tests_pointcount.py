from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from ..models import PointCount, Rating, Discount
import json
from django.urls import reverse
from collections import OrderedDict


class PointCountTest(TestCase):
    def setUp(self) -> None:
        self.c = APIClient()
        user_kw = dict(username='just_user', password='password', email='user@gmail.com')
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.superuser = User.objects.create_superuser(username='admin', email='admin@test.com', password='password')
        self.pointcount = PointCount.objects.get(user=self.user)

    def test_list_permissions(self):
        self.c.login(username=self.user.username,password='password')
        response = self.c.get('/api/accounts/pointcount/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data, OrderedDict(
            [('count', 1),
             ('next', None),
             ('previous', None),
             ('results', [
                 OrderedDict([("user", self.user.id),("points", 0.0)]),])]))


    def test_this_users_account_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/pointcount/{self.user.id}/')
        self.assertEqual(response.data,{'user': self.user.id, 'points': 0.0})
        self.assertEqual(response.data, {'user': self.user.id, 'points': 0.0})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_other_users_pointcount_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/pointcount/{self.superuser.id}/',follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_delete_object(self):
       self.c.login(username=self.user.username, password='password')
       response = self.c.delete(f'/api/accounts/pointcount/{self.user.id}/')
       self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_put(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.put(f'/api/accounts/pointcount/{self.user.id}/', {'points': 100}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.patch(f'/api/accounts/pointcount/{self.user.id}/', {'points': 100}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



    def test_put_superuser(self):
        self.c.force_login(self.superuser)
        data = {'points': 100,'user':self.user.id}
        response = self.c.put(f'/api/accounts/pointcount/{self.pointcount.pk}/', data, format='json', follow = True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,data)

    def test_patch_superuser(self):
        self.c.force_login(self.superuser)
        data = {'points': 1000}
        response = self.c.patch(f'/api/accounts/pointcount/{self.pointcount.pk}/',
                                data, format='json', follow = True)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'points':1000,'user':self.user.id})


    def test_delete_superuser(self):
        self.c.force_login(self.superuser)
        response = self.c.delete(f'/api/accounts/pointcount/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)