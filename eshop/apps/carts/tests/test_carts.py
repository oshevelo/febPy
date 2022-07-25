from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.carts.models import Cart, CartItem
from utils.helpers_for_tests import create_user, create_superuser
from .help_tests import create_product, create_cart_item


class CartTest(TestCase):
    def setUp(self):
        self.c = APIClient()
        self.user = create_user('serhii')
        self.superuser = create_superuser('admin')

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

    def test_cart_list_not_empty(self):

        self.cart = Cart.objects.create(user=self.user)
        self.product = create_product()
        self.cart_item = create_cart_item(cart=self.cart, product=self.product)
        self.c.login(username=self.user.username, password='111')
        response = self.c.get('/api/cart/')

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
                            "id": self.product.id,
                            "sku": "111",
                            "name": "test",
                            "price": '1000.00',
                            "amount_in_stock": 5
                        },
                        "quantity": 2,
                        "cost_product": 2000.0
                    }],
                    "total_price": 2000.0,
                    "created": response.data['results'][0]['created'],
                    "updated": response.data['results'][0]['updated']
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

    def test_cart_items_list_not_empty(self):
        self.cart = Cart.objects.create(user=self.user)
        self.product = create_product()
        self.cart_item = create_cart_item(cart=self.cart, product=self.product)
        self.c.login(username=self.user.username, password='111')
        url = reverse('cartitem-list', args=[self.cart.id])

        response = self.c.get(url)

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
                        "sku": "111",
                        "name": "test",
                        "price": "1000.00",
                        "amount_in_stock": 5
                    },
                    "quantity": 2,
                    "cost_product": 2000.00
                }
            ]
        })

    def test_create_cart_items(self):
        self.cart = Cart.objects.create(user=self.user)
        self.product = create_product()
        self.c.login(username=self.user.username, password='111')
        url = reverse('cartitem-list', args=[self.cart.id])

        response = self.c.post(
            url,
            data={
                "cart": self.cart.id,
                "product": {
                    "id": self.product.id
                },
                "quantity": 1
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_cart_items(self):
        self.cart = Cart.objects.create(user=self.user)
        self.product = create_product()
        self.product_2 = create_product(sku='2222', name='test update')
        self.cart_item = create_cart_item(cart=self.cart, product=self.product)
        self.c.login(username=self.user.username, password='111')
        url = reverse('cartitem-details', args=[self.cart.id, self.cart_item.id])

        response = self.c.put(
            url,
            data={
                "cart": self.cart.id,
                "product": {"id": self.product_2.id},
                "quantity": 4
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
                    "id": self.cart_item.id,
                    "cart": self.cart.id,
                    "product": {
                        "id": self.product_2.id,
                        "sku": "2222",
                        "name": "test update",
                        "price": "1000.00",
                        "amount_in_stock": 5
                    },
                    "quantity": 4,
                    "cost_product": 4000.00
        })

    # def test_update_quantity_cart_items(self):
    #     self.cart = Cart.objects.create(user=self.user)
    #     self.product = create_product()
    #     self.cart_item = create_cart_item(cart=self.cart, product=self.product, quantity=4)
    #     self.c.login(username=self.user.username, password='111')
    #     url = reverse('cartitem-details', args=[self.cart.id, self.cart_item.id])
    #
    #     response = self.c.patch(
    #         url,
    #         data={"quantity": 1},
    #         format='json'
    #     )
    #     print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, {
    #         "id": self.cart_item.id,
    #         "cart": self.cart.id,
    #         "product": {
    #             "id": self.product.id,
    #             "sku": "2222",
    #             "name": "test update",
    #             "price": "1000.00",
    #             "amount_in_stock": 5
    #         },
    #         "quantity": 1,
    #         "cost_product": 1000.00
    #     })

    def test_delete_cart_items(self):
        self.cart = Cart.objects.create(user=self.user)
        self.product = create_product()
        self.cart_item = create_cart_item(cart=self.cart, product=self.product)
        self.c.login(username=self.user.username, password='111')
        url = reverse('cartitem-details', args=[self.cart.id, self.cart_item.id])

        response = self.c.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_validate_quantity(self):
        self.cart = Cart.objects.create(user=self.user)
        self.product = create_product(amount_in_stock=3)
        self.cart_item = create_cart_item(cart=self.cart, product=self.product)
        self.c.login(username=self.user.username, password='111')
        url = reverse('cartitem-list', args=[self.cart.id])
        response = self.c.post(
            url,
            data={
                "cart": self.cart.id,
                "product": {
                    "id": self.product.id
                },
                "quantity": self.product.amount_in_stock + 1
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            "non_field_errors": [
                "Products is available: 3"
            ]
        })
