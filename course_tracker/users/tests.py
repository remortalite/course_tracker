from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse_lazy

from .models import User


class UsersTest(TestCase):
    fixtures = ['sample.json']

    def test_login_get(self):
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertIn(b'Login', response.content)

    def test_login_post(self):
        response = self.client.post(reverse_lazy('login'),
                                    follow=True,
                                    data={
                                        'username': 'test_user',
                                        'password': 'TQ3XxstZdj1CJf',
                                    })
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertIn(b'Login success', response.content)
        self.assertRedirects(response, reverse_lazy('home'))

    def test_logout(self):
        self.client.login(username='test_user', password='TQ3XxstZdj1CJf')

        response = self.client.post(reverse_lazy('logout'), follow=True)
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertIn(b'Logged out', response.content)

    def test_create_get(self):
        response = self.client.get(reverse_lazy('users.create'))

        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertIn(b'Create user', response.content)

    def test_create_post(self):
        response = self.client.post(reverse_lazy('users.create'),
                                    follow=True,
                                    data={
                                        'username': 'test_creation',
                                        'password1': 'TQ3XxstZdj1CJf',
                                        'password2': 'TQ3XxstZdj1CJf',
                                    })

        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertIn(b'User created', response.content)

        self.assertTrue(User.objects.filter(username='test_creation').exists())
