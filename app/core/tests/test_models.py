from django.test import TestCase
from core import models

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_email_is_successfull(self):
        email = 'example@example.com'
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test teh email for a new user is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'password')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@test.com', '1234')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def sample_user(email='test@londonappdev.com', password='testpass'):
        """Create a sample user"""
        return get_user_model().objects.create_user(email, password)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
