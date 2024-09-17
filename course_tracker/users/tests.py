from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse_lazy


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