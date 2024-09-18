from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse_lazy

from .models import User
from fixtures import fixture_loader


class UsersTest(TestCase):
    fixtures = ['sample.json']

    data = fixture_loader.load('course_tracker/'
                               'fixtures/data.json')

    def setUp(self):
        self.user = User.objects.get(username=self.data['user']['username'])
        self.another_user = User.objects.get(username='another_user')

    def _login(self):
        self.client.login(username=self.data['user']['username'],
                          password=self.data['user']['password'])

    def test_unauthorized_get(self):
        urls = [
            reverse_lazy('users.update', kwargs={'pk': self.user.id}),
        ]

        for url in urls:
            response = self.client.get(url, follow=True)

            self.assertEqual(response.status_code, HttpResponse.status_code)
            self.assertURLEqual(response.request['PATH_INFO'], reverse_lazy('login'))
            self.assertIn(b'You need to log in', response.content)

    def test_login_get(self):
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertIn(b'Login', response.content)

    def test_login_post(self):
        response = self.client.post(reverse_lazy('login'),
                                    follow=True,
                                    data=self.data['user'])
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
                                        'password1': self.data['user']['password'],
                                        'password2': self.data['user']['password'],
                                    })

        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertIn(b'User created', response.content)

        self.assertTrue(User.objects.filter(username='test_creation').exists())

    def test_update_get_auth(self):
        self._login()

        response = self.client.get(reverse_lazy('users.update',
                                                kwargs={'pk': self.user.id}),
                                   follow=True)

        self.assertEqual(response.status_code, HttpResponse.status_code)
        self.assertIn(b'Update user', response.content)
        self.assertIn(self.user.username.encode(), response.content)

    def test_update_post_no_auth(self):
        url_for_user = reverse_lazy('users.update', kwargs={'pk': self.user.id})
        response = self.client.post(url_for_user,
                                    follow=True,
                                    data={
                                        'first_name': 'Updated name',
                                        'username': 'test_update',
                                    })
        self.assertURLEqual(response.request['PATH_INFO'], reverse_lazy('login'))
        self.assertIn(b'You need to log in', response.content)

    def test_update_post_auth_restricted(self):
        url_for_user = reverse_lazy('users.update', kwargs={'pk': self.user.id})

        # test auth, not authorized
        self.client.login(username=self.another_user.username,
                          password=self.another_user.password)
        response = self.client.post(url_for_user,
                                    follow=True,
                                    data={
                                        'first_name': 'Updated name',
                                        'username': 'test_update',
                                    })
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertIn(b'Access forbidden',
                      response.content)

    def test_update_post_auth_access(self):
        url_for_user = reverse_lazy('users.update', kwargs={'pk': self.user.id})

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

        self.assertFalse(
            User.objects.filter(
                username=self.data['user']['username']
            ).exists())
        self.assertTrue(User.objects.get(username='test_update')
                        .first_name == 'Updated name')
