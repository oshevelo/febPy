from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from ..models import PointCount, Rating, Discount

class PointCountTest(TestCase):
   def setUp(self)->None:
      self.c = APIClient()
      user_kw = dict(username='just_user',password='password',email='user@gmail.com')
      user_kw['password'] = make_password(user_kw['password'])
      self.user = User.objects.create(**user_kw)


   def test_list_permissions(self):
    self.c.login(username=self.user.username,password='password')
    response = self.c.get('/api/accounts/pointcount')
    print(response.data)
    self.assertEqual(response.status_code,status.HTTP_200_OK)

   def test_this_users_account_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/pointcount/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

   def test_other_user_pointcount_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get('/api/accounts/pointcount/3')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# class DiscountTest(TestCase):

#
# class RatingTest(TestCase):
