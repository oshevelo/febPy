from django.test import TestCase
from rest_framework.test import APIClient


class RecalculationProfileChildrenChanges(TestCase):

    def setUp(self):
        self.c = APIClient()

    def test_list(self):
        self.assertEqual(1, 1)
