from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
<<<<<<< HEAD
from ..models import PointCount, Rating, Discount
import json
=======
# from ..models import PointCount, Rating, Discount
>>>>>>> a450a84692f979995c9be16c52868fbaa2267e0d
from django.urls import reverse


class PointCountTest(TestCase):
    def setUp(self) -> None:
        self.c = APIClient()
        user_kw = dict(username='just_user', password='password', email='user@gmail.com')
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.superuser = User.objects.create_superuser(username='admin', email='admin@test.com', password='password')

<<<<<<< HEAD
   def test_list_permissions(self):
    self.c.login(username=self.user.username,password='password')
    response = self.c.get('/api/accounts/pointcount/')
    self.assertEqual(response.status_code,status.HTTP_200_OK)
    self.assertEqual(len(response.data['results']),1)
    self.assertEqual(response.data['results'][0]['user'],self.user.id)
=======
    def test_list_permissions(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get('/api/accounts/pointcount/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        print(response.data['results'][0]['user'], self.user.id)
        self.assertEqual(response.data['results'][0]['user'], self.user.id)
>>>>>>> a450a84692f979995c9be16c52868fbaa2267e0d

    def test_this_users_account_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/pointcount/{self.user.id}/')
<<<<<<< HEAD
        self.assertEqual(response.data,{'user': self.user.id, 'points': 0.0}
)
=======
        print(response.data)
        self.assertEqual(response.data, {'user': self.user.id, 'points': 0.0}
                         )
>>>>>>> a450a84692f979995c9be16c52868fbaa2267e0d
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_users_pointcount_permission(self):
        self.c.login(username=self.user.username, password='password')
<<<<<<< HEAD
        response = self.c.get(f'/api/accounts/pointcount/{self.superuser.id}/',follow=True)
=======
        response = self.c.get(f'/api/accounts/pointcount/3/', follow=True)
        print('response other user', response.status_code)
>>>>>>> a450a84692f979995c9be16c52868fbaa2267e0d
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # конечно, здесь и будет возвращаться 404, потому что объекта с id=3 попросту нет. Т.е. это тест на
        # наличие объекта, а не на действие permissions

    def test_delete_object(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.delete(f'/api/accounts/pointcount/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

<<<<<<< HEAD
   def test_delete_object(self):
       self.c.login(username=self.user.username, password='password')
       response = self.c.delete(f'/api/accounts/pointcount/{self.user.id}/')
       self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


   def test_put(self):
       self.c.login(username=self.user.username, password='password')
       response = self.c.put(f'/api/accounts/pointcount/{self.user.id}',
                             {'points': 100}, format='json', follow=True)
       self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
=======
    def test_put(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.put(f'/api/accounts/pointcount/{self.user.id}/', {'points': 100}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # нужно попробовать такой же тест провести под суперюзером, чтобы убедиться, что суперюзер может делать PUT
>>>>>>> a450a84692f979995c9be16c52868fbaa2267e0d
