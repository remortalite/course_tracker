from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse_lazy

from .models import User


class UsersTest(TestCase):
    fixtures = ['sample.json']

    def setUp(self):
        self.user_data = {
            'username': 'test_user',
            'password': 'TQ3XxstZdj1CJf',
        }

        self.user = User.objects.get(username='test_user')

    def _login(self):
        self.client.login(**self.user_data)

    def test_login_get(self):
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertIn(b'Login', response.content)

    def test_login_post(self):
        response = self.client.post(reverse_lazy('login'),
                                    follow=True,
                                    data=self.user_data)
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertIn(b'Login success', response.content)
        self.assertRedirects(response, reverse_lazy('home'))

    def test_logout(self):
        self._login()

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
                                        'password1': self.user_data['password'],
                                        'password2': self.user_data['password'],
                                    })

        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertIn(b'User created', response.content)

        self.assertTrue(User.objects.filter(username='test_creation').exists())

    def test_update_get_no_auth(self):
        response = self.client.get(reverse_lazy('users.update',
                                                kwargs={'pk': self.user.id}),
                                   follow=True)

        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertURLEqual(response.request['PATH_INFO'], reverse_lazy('login'))
        # self.assertIn(b'You need to log in', response.content)

    def test_update_get_auth(self):
        self._login()

        response = self.client.get(reverse_lazy('users.update',
                                                kwargs={'pk': self.user.id}),
                                   follow=True)

        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertIn(b'Update user', response.content)
        self.assertIn(b'test_user', response.content)

    def test_update_post_no_auth(self):
        another_user = User.objects.create_user(username='another_user',
                                                password='another_password')
        url_for_user = reverse_lazy('users.update', kwargs={'pk': self.user.id})

        # test unauth
        response = self.client.post(url_for_user,
                                    follow=True,
                                    data={
                                        'first_name': 'Updated name',
                                        'username': 'test_update',
                                    })
        self.assertURLEqual(response.request['PATH_INFO'], reverse_lazy('login'))
        # self.assertIn(b'You need to log in', response.content)

    def test_update_post_auth_restricted(self):
        another_user = User.objects.create_user(username='another_user',
                                                password='another_password')
        url_for_user = reverse_lazy('users.update', kwargs={'pk': self.user.id})

        # test auth, not authorized
        self.client.login(username='another_user',
                          password='another_password')
        response = self.client.post(url_for_user,
                                    follow=True,
                                    data={
                                        'first_name': 'Updated name',
                                        'username': 'test_update',
                                    })
        self.assertRedirects(response, reverse_lazy('home'))
        # self.assertIn(b'Another user updation is forbidden',
        #               response.content)

    def test_update_post_auth_access(self):
        url_for_user = reverse_lazy('users.update', kwargs={'pk': self.user.id})

        # authorized
        self._login()

        response = self.client.post(url_for_user,
                                    follow=True,
                                    data={
                                        'first_name': 'Updated name',
                                        'username': 'test_update',
                                    })

        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertIn(b'User updated', response.content)

        self.assertFalse(User.objects.filter(username='test_user').exists())
        self.assertTrue(User.objects.get(username='test_update')
                        .first_name == 'Updated name')
