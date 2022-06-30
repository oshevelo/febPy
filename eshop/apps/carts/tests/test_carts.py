from django.contrib.auth.hashers import make_password
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from apps.carts.models import Cart, CartItem
from django.contrib.auth.models import User
from apps.products.models import Product


class CartTest(TestCase):
    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='azzyyy',
            password='111',
            email='azzyyy' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)

    def test_list_check_permission(self):
        response = self.c.get('/api/cart/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cart_list_empty(self):
        self.c.login(username=self.user.username, password='111')
        response = self.c.get('/api/cart/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        })

    def test_cart_list_no_empty(self):

        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(
            sku='11111',
            name='phone',
            description='description phone',
            price=1000,
            amount_in_stock=5,
        )
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )
        self.c.login(username=self.user.username, password='111')
        response = self.c.get('/api/cart/')

        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 2,
                    "user": self.user.id,
                    "cart_items": [{
                        "id": 2,
                        "cart": 2,
                        "product": {
                            "id": 2,
                            "sku": "11111",
                            "name": "phone",
                            "price": '1000.00',
                            "amount_in_stock": 5
                        },
                        "quantity": 2,
                        "cost_product": 2000.0
                    }],
                    "total_price": 2000.0,
                    "created": self.cart.created.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                    "updated": self.cart.updated.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                }
            ]
        })

    def test_create_cart(self):
        self.c.login(username=self.user.username, password='111')
        response = self.c.post(
            '/api/cart/',
            data={
                "user": self.user.id,
                "cart_items": []
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cart_items_list_no_empty(self):
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(
            sku='77777',
            name='phone 10',
            description='description phone',
            price=5000,
            amount_in_stock=5,
        )
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )
        self.c.login(username=self.user.username, password='111')
        response = self.c.get('/api/cart/1/cartitem')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "cart": 1,
                    "product": {
                        "id": 1,
                        "sku": "77777",
                        "name": "phone 10",
                        "price": "5000.00",
                        "amount_in_stock": 5
                    },
                    "quantity": 2,
                    "cost_product": 10000.00
                }
            ]
        })

    def test_create_cart_items(self):
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(
            sku='765431',
            name='Sony Playstation',
            description='description PS',
            price=5900,
            amount_in_stock=5,
        )
        self.c.login(username=self.user.username, password='111')
        response = self.c.post(
            '/api/cart/4/cartitem',
            data={
                "cart": 4,
                "product": {
                    "id": self.product.id
                },
                "quantity": 1
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_validate_quantity(self):
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(
            sku='123456',
            name='phone 77',
            description='description phone',
            price=2000,
            amount_in_stock=3,
        )
        self.cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )
        self.c.login(username=self.user.username, password='111')
        response = self.c.post(
            '/api/cart/3/cartitem',
            data={
                "cart": self.cart.id,
                "product": {
                    "id": self.product.id
                },
                "quantity": self.product.amount_in_stock + 1
            },
            format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "non_field_errors": [
                f"Products is available: 3"
            ]
        })










