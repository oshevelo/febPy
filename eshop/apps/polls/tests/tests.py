from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from apps.polls.models import Question
from collections import OrderedDict
from datetime import datetime
from django.utils import timezone


class RecalculationProfileChildrenChanges(TestCase):

    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='asmin',
            password='111',
            email='asmin' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)

    def test_list_check_permission(self):
        response = self.c.get('/api/polls/question/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_empty(self):
        self.c.login(username=self.user.username, password='111')
        response = self.c.get('/api/polls/question/')

        print(response.data)
        # print(dir(status))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        })

    # def test_list_empty(self):
    #     new_question = Question.objects.create(question_text='asdasd', pub_date=datetime.now())
    #     new_question = Question.objects.create(question_text='asdasd', pub_date=datetime.now(), author=self.user)
    #     self.c.login(username=self.user.username, password='111')
    #     response = self.c.get('/api/polls/question/')
    #
    #     print(response.data)
    #     # print(dir(status))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, {
    #         "count": 0,
    #         "next": None,
    #         "previous": None,
    #         "results": []
    #     })
        
