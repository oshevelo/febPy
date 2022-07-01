from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from apps.feedbacks.models import Feedback
from utils.helpers_for_tests import create_user, create_superuser


class FeedbackTest(TestCase):
    def setUp(self):
        self.c = APIClient()
        self.super_admin = create_superuser("odin")
        self.no_admin = create_user("pedro")

    def test_list_check_permission(self):
        response = self.c.get('/feedback/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_empty(self):
        self.c.login(username=self.super_admin.username, password='111')
        response = self.c.get('/feedback/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        })

    def test_list_no_empty(self):
        Feedback.objects.create(user=self.super_admin, user_phone='+380320987654',
                                subject='DP',
                                feedback='How are you?',
                                is_published=True)
        self.c.force_login(self.super_admin)
        response = self.c.get('/feedback/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "user": "odin",
                    "user_email": "odin@email.com",
                    "user_phone": '+380320987654',
                    "subject": "DP",
                    "feedback": "How are you?",
                    "is_published": True
                }
            ]
        })

    def tests_create_feedback_from_superuser(self):
        self.c.force_login(self.super_admin)
        response = self.c.post('/feedback/', data={
            "user_phone": "+380981234567",
            "subject": 'DP',
            "feedback": "test feedback from superuser",
            "is_published": True
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def tests_create_feedback_from_user(self):
        self.c.force_login(self.no_admin)
        response = self.c.post('/feedback/', data={
            "user_phone": "+380981234567",
            "subject": 'DP',
            "feedback": "test feedback from superuser",
            "is_published": True
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def tests_delete_not_own_feedback_from_user(self):
        self.c.force_login(self.super_admin)
        self.c.post('/feedback/', data={
            "user_phone": "+380981234567",
            "subject": 'DP',
            "feedback": "test feedback from superuser",
            "is_published": True
        }, format='json')
        self.c.logout()

        self.c.force_login(self.no_admin)
        feedback = Feedback.objects.filter(user=self.super_admin).first()
        url = reverse('feedbacks:feedback-by-id', args=[feedback.id])
        response = self.c.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tests_delete_own_feedback_from_user(self):
        self.c.force_login(self.no_admin)
        url = reverse('feedbacks:feedback-list', )
        self.c.post(url, data={
            "user_phone": "+380981234567",
            "subject": 'DP',
            "feedback": "test feedback from superuser",
            "is_published": True
        }, format='json')
        feedback = Feedback.objects.filter(user=self.no_admin).first()
        delete_url = reverse('feedbacks:feedback-by-id', args=[feedback.id])
        response = self.c.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def tests_delete_not_own_feedback_from_superuser(self):
        self.c.force_login(self.no_admin)
        url = reverse('feedbacks:feedback-list', )
        self.c.post(url, data={
            "user_phone": "+380981234567",
            "subject": 'DP',
            "feedback": "test feedback from superuser",
            "is_published": True
        }, format='json')
        self.c.logout()

        self.c.force_login(self.super_admin)
        feedback = Feedback.objects.filter(user=self.no_admin).first()
        delete_url = reverse('feedbacks:feedback-by-id', args=[feedback.id])
        response = self.c.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def tests_update_own_feedback_from_user(self):
        self.c.force_login(self.no_admin)
        url = reverse('feedbacks:feedback-list', )
        self.c.post(url, data={
            "user_phone": "+380981234567",
            "subject": 'DP',
            "feedback": "test feedback from superuser",
            "is_published": True
        }, format='json')
        feedback = Feedback.objects.filter(user=self.no_admin).first()
        update_url = reverse('feedbacks:feedback-by-id', args=[feedback.id])
        response = self.c.patch(update_url, data={'feedback': 'new test feedback'})
        feedback_upd = Feedback.objects.filter(user=self.no_admin).first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(feedback_upd.feedback, 'new test feedback')
