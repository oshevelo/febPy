from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from ..models import PointCount,Rating,Discount

class PointCountTest(TestCase):
    def setUp(self)->None:
        self.c = APIClient()
        user_kw = dict(username='just_user',password='password',email='user@gmail.com')
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)

    def test_object_permission(self):
        response = self.c.get('accounts/pointcount')
        print(response.status_code)
        self.assertEqual(response.status_code,status.HTTP_202_OK)
   #def test_object_list_permission()

#class DiscountTest(TestCase):

#
#class RatingTest(TestCase):


