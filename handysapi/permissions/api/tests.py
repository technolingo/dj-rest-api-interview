from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
User = get_user_model()

from datetime import date


class APIPermissionsTestCase(APITestCase):
    '''Test custom permission inheritance and status codes'''
    
    def setUp(self):
        user = User.objects.create(
            email='hello@example.com',
            birthday=date.today(),
            membership_status='0'
        )
        user.set_password('simpleSecret123')
        user.save()

    def test_list_permission_fail(self):
        url = api_reverse('permissions:list')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(status_boolean)

    def test_list_permission_success(self):
        token = Token.objects.get(user__email='hello@example.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = api_reverse('permissions:list')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(status_boolean)

    def test_view_permission_fail(self):
        token = Token.objects.get(user__email='hello@example.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = api_reverse('permissions:view')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(status_boolean)

    def test_view_permission_success(self):
        token = Token.objects.get(user__email='hello@example.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # change membership code to grant permission
        user = User.objects.get(email='hello@example.com')
        user.membership_status = '1'
        user.save()

        url = api_reverse('permissions:view')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(status_boolean)

    def test_edit_permission_fail(self):
        url = api_reverse('permissions:edit')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(status_boolean)

    def test_edit_permission_success(self):
        token = Token.objects.get(user__email='hello@example.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = api_reverse('permissions:edit')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(status_boolean)

    def test_delete_permission_fail(self):
        token = Token.objects.get(user__email='hello@example.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # change membership code to deny permission
        user = User.objects.get(email='hello@example.com')
        user.membership_status = '1'
        user.save()

        url = api_reverse('permissions:delete')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(status_boolean)

    def test_delete_permission_success(self):
        token = Token.objects.get(user__email='hello@example.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # change membership code to grant permission
        user = User.objects.get(email='hello@example.com')
        user.membership_status = '2'
        user.save()

        url = api_reverse('permissions:delete')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(status_boolean)
