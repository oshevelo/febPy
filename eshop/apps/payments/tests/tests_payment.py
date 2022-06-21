from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.payments.models import Payment
from utils.helpers_for_tests import create_user, create_superuser


class PaymentTest(TestCase):

    def setUp(self):
        self.c = APIClient()
        self.super_admin = create_superuser("admin")
        self.no_admin = create_user("jora")

    def test_list_check_permission(self):
        response = self.c.get('/api/payment/pay/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_empty(self):
        self.c.login(username=self.super_admin.username, password='111')
        response = self.c.get('/api/payment/pay/')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        })

    def test_list(self):
        Payment.objects.create(owner=self.super_admin,
                               system='Liqpay',
                               status='Completed',
                               products_price=1212,
                               delivery_price=111
                               )
        self.c.force_login(self.super_admin)
        response = self.c.get('/api/payment/pay/')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    'owner': 'admin',
                    'id': 1,
                    'system': 'Liqpay',
                    'status': 'Completed',
                    'products_price': 1212,
                    'delivery_price': 111,
                }
            ]
        })
