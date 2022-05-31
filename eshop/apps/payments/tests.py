from django.test import TestCase
from rest_framework.test import APIClient


class SmthTest(TestCase):
    def setUp(self):
        self.c = APIClient()

    def test_list(self):
        self.assertEqqual(1, 1)




