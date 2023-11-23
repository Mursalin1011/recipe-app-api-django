from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""

        email = 'test@example.com'
        password = 'Testpass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        """Test user email for normalized"""
        email = 'test@EXAMPLE.COM'
        password = 'Testpass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com', 'test12345'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
