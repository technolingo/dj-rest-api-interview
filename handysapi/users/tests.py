from rest_framework.authtoken.models import Token

from django.test import TestCase
from .models import User

from datetime import date


class UserTestCase(TestCase):
    '''A simple test case for user creation and token generation'''

    def setUp(self):
        user = User.objects.create(
            email='hello@example.com',
            birthday=date.today(),
            membership_status='0'
        )
        user.set_password('simpleSecret123')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(email='hello@example.com')
        self.assertEqual(qs.count(), 1)

    def test_generated_token(self):
        qs = Token.objects.filter(user__email='hello@example.com')
        self.assertEqual(qs.count(), 1)

    def test_membership_status(self):
        user = User.objects.filter(email='hello@example.com').first()
        self.assertEqual(user.get_membership_int(), 0)
