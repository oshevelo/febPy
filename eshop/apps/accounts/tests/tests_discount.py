from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from ..models import PointCount, Rating, Discount
from django.urls import reverse

class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.c = APIClient()
        user_kw = dict(username='just_user', password='password', email='user@gmail.com')
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.superuser = User.objects.create_superuser('admin', 'admin@test.com', 'password')

    def test_list_permissions(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get('/api/accounts/discount',follow=True)
#        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        #print(response.data['results'][0]['user'], self.user.id)
        self.assertEqual(response.data['results'][0]['user'], self.user.id)

    def test_this_users_discount_permission(self):
        self.c.login(username=self.user.username, password='password')
        # print(f'/api/accounts/pointcount/{self.user.id}/')
        response = self.c.get(f'/api/accounts/discount/{self.user.id}/')
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_users_discount_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/discount/6', follow=True)
        #print('response other user', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_discount(self):
        self.users_discount = Discount.objects.get(pk=self.user.id)
        self.c.login(username=self.user.username, password='password')
        response = self.c.put(f'api/accounts/discount/{self.user.id}',
                              data={'id': self.users_pointcount.id,
                                    'discount': 0.4, 'pointcount':self.user.pointcount.id,'prev_count':5000}, format='json')
        print('Put response', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_discount(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.delete(f'api/accounts/2')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def delete_discount_superuser(self):
        self.c.login(username=self.superuser.username, password=self.superuser.password)
        response = self.c.delete(f'api/accounts/2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_discount_superuser(self):
        self.c.login(username=self.superuser.username, password=self.superuser.password)
        response = self.c.get('api/accounts/pointcount/5')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_discount_superuser(self):
        self.c.login(username=self.superuser.username, password=self.superuser.password)
        response = self.c.put(f'api/accounts/pointcount/3',
                              data={'pointcount': 3, 'user': 3,
                                    'points': 104}, format='json')
        print('Put respon', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
