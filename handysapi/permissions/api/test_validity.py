from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework.authtoken.models import Token

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

User = get_user_model()

from datetime import date


class APIPermissionsTestCase(APITestCase):
    '''Test custom permission inheritance and status codes'''

    def setUp(self):
        user = User.objects.create(
            email='hello@example.com',
            birthday=date.today()
        )
        user.set_password('simpleSecret123')
        user.save()

    def test_list_permission_unauthorized(self):
        url = api_reverse('permissions:list')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(status_boolean)

    def test_list_permission_forbidden(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = api_reverse('permissions:list')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(status_boolean)

    def test_list_permission_success(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # grant permission programmatically
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(
            codename='can_list_dummy',
            content_type=content_type,
        )
        user.user_permissions.add(permission)

        url = api_reverse('permissions:list')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(status_boolean)

    def test_view_permission_unauthorized(self):
        url = api_reverse('permissions:view')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(status_boolean)

    def test_view_permission_forbidden(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = api_reverse('permissions:view')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(status_boolean)

    def test_view_permission_success(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # grant permission programmatically
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(
            codename='can_view_dummy',
            content_type=content_type,
        )
        user.user_permissions.add(permission)

        url = api_reverse('permissions:view')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(status_boolean)

    def test_edit_permission_unauthorized(self):
        url = api_reverse('permissions:edit')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(status_boolean)

    def test_edit_permission_forbidden(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = api_reverse('permissions:edit')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(status_boolean)

    def test_edit_permission_success(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # grant permission programmatically
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(
            codename='can_edit_dummy',
            content_type=content_type,
        )
        user.user_permissions.add(permission)

        url = api_reverse('permissions:edit')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(status_boolean)

    def test_delete_permission_unauthorized(self):
        url = api_reverse('permissions:delete')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(status_boolean)

    def test_delete_permission_forbidden(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = api_reverse('permissions:delete')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(status_boolean)

    def test_delete_permission_success(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # grant permission programmatically
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(
            codename='can_delete_dummy',
            content_type=content_type,
        )
        user.user_permissions.add(permission)

        url = api_reverse('permissions:delete')
        r = self.client.get(url, format='json')
        status_boolean = r.data.get('success')

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(status_boolean)

    def tearDown(self):
        user = User.objects.get(email='hello@example.com')
        user.delete()
