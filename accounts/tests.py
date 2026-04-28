from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_register(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'test@test.com',
            'password1': 'StrongPass123',
            'password2': 'StrongPass123'
        })
        self.assertEqual(response.status_code, 302)  # redirect

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)

    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # redirect to login

    def test_logged_in_user_can_access_profile(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)