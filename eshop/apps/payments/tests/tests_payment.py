from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.payments.models import Payment
from utils.helpers_for_tests import create_user, create_superuser


class PaymentTest(TestCase):

    def setUp(self):
        self.c = APIClient()
        self.super_admin = create_superuser('georgii')
        self.no_admin = create_user('jora')

    def test_list_check_permissions(self):
        response = self.c.get('/api/payment/pay/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_empty(self):
        self.c.login(username=self.super_admin.username, password='111')
        response = self.c.get('/api/payment/pay/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        })

    def test_list_no_empty(self):
        Payment.objects.create(owner=self.super_admin,
                               system='Liqpay',
                               status='Completed',
                               products_price=1212,
                               delivery_price=111
                               )
        self.c.login(username=self.super_admin.username, password='111')
        response = self.c.get('/api/payment/pay/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {
                    'owner': 'georgii',
                    'id': 2,
                    'system': 'Liqpay',
                    'status': 'Completed',
                    'products_price': '1212.00',
                    'delivery_price': '111.00'
                }
            ]
        })

    def test_create_payment_as_superuser(self):
        self.c.force_login(self.super_admin)
        response = self.c.post('/api/payment/pay/', data={
            'system': 'PayPal',
            'status': 'Processing',
            'products_price': '1412',
            'delivery_price': '121'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': 1,
            'system': 'PayPal',
            'status': 'Processing',
            'products_price': '1412.00',
            'delivery_price': '121.00'
        })

    def test_create_payment_as_anonym(self):
        response = self.c.post('/api/payment/pay/', data={
            'system': 'PayPal',
            'status': 'Processing',
            'products_price': '999',
            'delivery_price': '47'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_payment_delete(self):
        self.c.force_login(self.super_admin)
        self.c.post('/api/payment/pay/', data={
            'system': 'PayPal',
            'status': 'Processing',
            'products_price': '1222',
            'delivery_price': '555'
        }, format='json')
        response = self.c.delete('/api/payment/pay/3/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_payment_detail(self):
        self.c.force_login(self.super_admin)
        self.c.post('/api/payment/pay/', data={
            'system': 'PayPal',
            'status': 'Processing',
            'products_price': '4321',
            'delivery_price': '99'
        }, format='json')
        response = self.c.get('/api/payment/pay/4/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 4,
            'system': 'PayPal',
            'status': 'Processing',
            'products_price': '4321.00',
            'delivery_price': '99.00'
        })

    def test_payment_update(self):
        self.c.force_login(self.super_admin)
        self.c.post('/api/payment/pay/', data={
            'system': 'PayPal',
            'status': 'Processing',
            'products_price': '4212',
            'delivery_price': '42'
        }, format='json')
        response = self.c.put('/api/payment/pay/5/', data={
            'system': 'Liqpay',
            'products_price': '422',
            'delivery_price': '33'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 5,
            'system': 'Liqpay',
            'status': 'Processing',
            'products_price': '422.00',
            'delivery_price': '33.00'
        })

    def test_payment_validate(self):
        self.c.force_login(self.super_admin)
        self.c.post('/api/payment/pay/', data={
            'system': 'PayPal',
            'status': 'Processing',
            'products_price': '4212',
            'delivery_price': '42'
        }, format='json')
        response = self.c.put('/api/payment/pay/6/', data={
            'system': 'Liqpay',
            'products_price': '11',
            'delivery_price': '999'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_detail_permission(self):
        response = self.c.get('/api/payment/pay/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_log_list_permission(self):
        response = self.c.get('/api/payment/log/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_log_list_empty(self):
        self.c.login(username=self.super_admin, password='111')
        response = self.c.get('/api/payment/log/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        })

    def test_log_detail_permission(self):
        response = self.c.get('/api/payment/log/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
