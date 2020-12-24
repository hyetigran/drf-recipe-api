from django.test import TestCase

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
