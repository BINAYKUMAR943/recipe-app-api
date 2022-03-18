from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a user with an email"""
        email="binay943@gmail.com"
        password="Nov@1995"
        user=get_user_model().objects.create_user(email,password)
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):

        """Test that domain part of the email is case in-sensitive"""
        email="binaykumar@GMAIL.COM"
        user=get_user_model().objects.create_user(email,"test123")
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test that new user creating account with email raise errors"""

        with self.assertRaises(ValueError):
            user=get_user_model().objects.create_user(None,"test123")

    def test_create_super_user(self):
        """Test of creating superuser"""
        user=get_user_model().objects.create_superuser("binay943@gmail.com","test123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
