
# Create your tests here.
from django.test import TestCase
from apps.orders.models import Order, OrderItem
from rest_framework.test import APIClient
from  rest_framework import status
from django.contrib.auth.models import User


class OrderTest(TestCase):
    def setUp(self):
        self.c = APIClient()

    def test_list_check_permission(self):
        response = self.c.get('/api/orders/order')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list(self):
        self.c.login(username=self.user.username, password="111")
        response = self.c.get('/api/orders/order')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data, {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        })



