from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from ..models import PointCount, Rating, Discount
from collections import OrderedDict


class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.c = APIClient()
        user_kw = dict(username='just_user', password='password', email='user@gmail.com')
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.superuser = User.objects.create_superuser(username='admin', email='admin@test.com', password='password')


    def test_list_permissions(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get('/api/accounts/discount/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data, OrderedDict(
            [('count',1),
             ('next',None),
             ('previous',None),
             ('results', [
                OrderedDict([("user", self.user.id),
                            ("pointcount", OrderedDict([("points", 0.0), ("id", self.user.id)])),
                             ("discount", 0.05),
                             ("prev_count", 0.0)]),
            ])])
        )

    def test_this_users_account_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/discount/{self.user.id}/')
        self.assertEqual(response.data,
                         {"user":self.user.id,
                          "pointcount":OrderedDict([("points",0.0),("id",self.user.id)]),
                          "discount":0.05,
                          "prev_count":0.0})


        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_other_users_pointcount_permission(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.get(f'/api/accounts/discount/{self.user.id-1}/', follow=True)
        print('response other user', response.status_code)
        print(self.user.id)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_delete_object(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.delete(f'/api/accounts/discount/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_put(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.put(f'/api/accounts/discount/{self.user.id}/', {'discount': 0.1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch(self):
        self.c.login(username=self.user.username, password='password')
        response = self.c.patch(f'/api/accounts/discount/{self.user.id}/', {'discount': 0.1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_put_superuser(self):
        self.c.force_login(self.superuser)
        response = self.c.put(f'/api/accounts/discount/{self.user.id}',
                              {"user": self.user.id,
                               "pointcount": OrderedDict([("points", 0.0), ("id", self.user.id)]),
                               "discount": 0.9,
                               "prev_count": 100.0}
                              , format='json', follow = True)

        obj = Discount.objects.get(user=self.user.id)
        obj.refresh_from_db()

        self.assertEqual(response.data, {"user": self.user.id,
                                         "pointcount": OrderedDict([("points", 0.0),
                                                                    ("id", self.user.id)]),
                                         "discount": 0.9,
                                         "prev_count": 100.0})

        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_patch_superuser(self):
        self.c.force_login(self.superuser)
        response = self.c.patch(f'/api/accounts/discount/{self.user.id}',
                              {"user": self.user.id,
                               "pointcount": OrderedDict([("points", 0.0), ("id", self.user.id)]),
                               "discount": 0.9,
                               "prev_count": 100.0}
                              , format='json', follow = True)

        obj = Discount.objects.get(user=self.user.id)
        obj.refresh_from_db()

        self.assertEqual(response.data, {"user": self.user.id,
                                         "pointcount": OrderedDict([("points", 0.0),
                                                                    ("id", self.user.id)]),
                                         "discount": 0.9,
                                         "prev_count": 100.0})

        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_delete_superuser(self):
        self.c.force_login(self.superuser)
        response = self.c.delete(f'/api/accounts/discount/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)