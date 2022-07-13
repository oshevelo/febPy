from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from ..models import PointCount, Rating, Discount
from django.urls import reverse

class RatingTest(TestCase):
    def setUp(self) -> None:
        self.c = APIClient()
        user_kw = dict(username='just_user', password='password', email='user@gmail.com')
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.superuser = User.objects.create_superuser('admin', 'admin@test.com', 'password')

    def test_list_permissions(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get('/api/accounts/rating',follow=True)
#        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['user'], self.user.id)

    def test_this_users_discount_permission(self):
        self.c.login(username=self.user.username, password='password')
        # print(f'/api/accounts/pointcount/{self.user.id}/')
        response = self.c.get(f'/api/accounts/rating/{self.user.id}/')
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_users_discount_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/rating/6', follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_discount(self):
        self.users_rating = Rating.objects.get(pk=self.user.id)
        self.c.login(username=self.user.username, password='password')
        response = self.c.put(f'api/accounts/rating/{self.user.id}',
                              data={'rating': self.users_rating.id,
                                    'percentile': 0.99,'pointcount':self.users_rating.pointcount.id}, format='json')
        print('Put response', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

