# Create your tests here.
from django.contrib.auth.hashers import make_password
from django.test import TestCase
from apps.orders.models import Order, OrderItem
from apps.products.models import Product
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User


class OrderTest(TestCase):
    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='admin',
            password='111',
            email='admin' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)

    def test_list_1(self):
        self.assertEqual(1, 1)

    def test_list_check_permission(self):
        response = self.c.get('/api/orders/order')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        # print(response.data)

    def test_list_orders_empty(self):
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

    def test_list_orders(self):
        self.order = Order.objects.create(user=self.user)
        self.product = Product.objects.create(
            sku='00001',
            name='asics_socks',
            description='asics sport socks',
            price=100,
            amount_in_stock=100
        )

        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3
        )
        self.c.login(username=self.user.username, password="111")
        response = self.c.get('/api/orders/order')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "user": self.user.id,
                    "order_items": [{
                        "id": 1,
                        "order": 1,
                        "product": {
                            "sku": '00001',
                            "name": 'asics_socks',
                            "description": 'asics sport socks',
                            "price": 100,
                            "amount_in_stock": 100
                        }
                    }]
                }
            ]
        })

    def test_create_order(self):
        self.c.login(username=self.user.username, password='111')
        response = self.c.post(
            '/api/orders/order/',
            data={
                "user": self.user.id,
                "order_items": []
                },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_order_items_list(self):
        self.order = Order.objects.create(user=self.user)
        self.product = Product.objects.create(
            sku='00005',
            name='asics_hat',
            description='asics hat',
            price=200,
            amount_in_stock=100,
        )

        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3
        )

        self.c.login(username=self.user.username, password="111")
        response = self.c.get('/api/orders/order/1/order_item')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "order": 1,
                    "product": {
                        "sku": '00005',
                        "name": 'asics_hat',
                        "description": 'asics hat',
                        "price": 200,
                        "amount_in_stock": 100
                    },
                    "quantity": 3
                }
            ]
        })

    def test_create_order_items(self):
        self.order = Order.objects.create(user=self.user)
        self.product = Product.objects.create(
            sku='00006',
            name='asics_shorts',
            description='asics shorts',
            price=300,
            amount_in_stock=50,
        )

        self.c.login(username=self.user.username, password="111")
        response = self.c.post(
            '/api/orders/order/1/order_item',
            data={
                "order": 3,
                "product": {
                    "id": self.product.id
                },
                "quantity": 2
            },
            format='json'
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




