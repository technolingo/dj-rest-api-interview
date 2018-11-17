from django.test import TestCase
from django.contrib.auth import get_user_model

from datetime import date

User = get_user_model()


class PermissionTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(
            email='hello@example.com',
            birthday=date.today(),
            membership_status='0'
        )
        user.set_password('simpleSecret123')
        user.save()

    def created_user(self):
        qs = User.objects.filter(email='hello@example.com')
        self.assertEqual(qs.count(), 1) # email uniqueness
        
