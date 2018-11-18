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

    def test_list_permission_inheritance(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.assertFalse(user.has_perm('users.can_list_dummy'))
        # grant permission programmatically
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(
            codename='can_list_dummy',
            content_type=content_type,
        )
        user.user_permissions.add(permission)
        # refetch user obj to let the permission take effect
        user = User.objects.get(email='hello@example.com')
        self.assertTrue(user.has_perm('users.can_list_dummy'))

        r_list = self.client.get(api_reverse('permissions:list'), format='json')
        r_view = self.client.get(api_reverse('permissions:view'), format='json')
        r_edit = self.client.get(api_reverse('permissions:edit'), format='json')
        r_delete = self.client.get(api_reverse('permissions:delete'), format='json')

        self.assertEqual(r_list.status_code, status.HTTP_200_OK)
        # List 귄한은 자식이 없다
        self.assertEqual(r_view.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(r_edit.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(r_delete.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_permission_inheritance(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.assertFalse(user.has_perm('users.can_view_dummy'))
        # grant permission programmatically
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(
            codename='can_view_dummy',
            content_type=content_type,
        )
        user.user_permissions.add(permission)
        # refetch user obj to let the permission take effect
        user = User.objects.get(email='hello@example.com')
        self.assertTrue(user.has_perm('users.can_view_dummy'))

        r_list = self.client.get(api_reverse('permissions:list'), format='json')
        r_view = self.client.get(api_reverse('permissions:view'), format='json')
        r_edit = self.client.get(api_reverse('permissions:edit'), format='json')
        r_delete = self.client.get(api_reverse('permissions:delete'), format='json')

        self.assertEqual(r_view.status_code, status.HTTP_200_OK)
        # View 귄한은 List란 자식이 있다
        self.assertEqual(r_list.status_code, status.HTTP_200_OK)
        self.assertEqual(r_edit.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(r_delete.status_code, status.HTTP_403_FORBIDDEN)

    def test_edit_permission_inheritance(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.assertFalse(user.has_perm('users.can_edit_dummy'))
        # grant permission programmatically
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(
            codename='can_edit_dummy',
            content_type=content_type,
        )
        user.user_permissions.add(permission)
        # refetch user obj to let the permission take effect
        user = User.objects.get(email='hello@example.com')
        self.assertTrue(user.has_perm('users.can_edit_dummy'))

        r_list = self.client.get(api_reverse('permissions:list'), format='json')
        r_view = self.client.get(api_reverse('permissions:view'), format='json')
        r_edit = self.client.get(api_reverse('permissions:edit'), format='json')
        r_delete = self.client.get(api_reverse('permissions:delete'), format='json')

        self.assertEqual(r_edit.status_code, status.HTTP_200_OK)
        # Edit 귄한은 View란 자식이 있다
        self.assertEqual(r_view.status_code, status.HTTP_200_OK)
        self.assertEqual(r_list.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(r_delete.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_permission_inheritance(self):
        user = User.objects.get(email='hello@example.com')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.assertFalse(user.has_perm('users.can_delete_dummy'))
        # grant permission programmatically
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(
            codename='can_delete_dummy',
            content_type=content_type,
        )
        user.user_permissions.add(permission)
        # refetch user obj to let the permission take effect
        user = User.objects.get(email='hello@example.com')
        self.assertTrue(user.has_perm('users.can_delete_dummy'))

        r_list = self.client.get(api_reverse('permissions:list'), format='json')
        r_view = self.client.get(api_reverse('permissions:view'), format='json')
        r_edit = self.client.get(api_reverse('permissions:edit'), format='json')
        r_delete = self.client.get(api_reverse('permissions:delete'), format='json')

        self.assertEqual(r_delete.status_code, status.HTTP_200_OK)
        # Delete 귄한은 Edit란 자식이 있다
        self.assertEqual(r_edit.status_code, status.HTTP_200_OK)
        self.assertEqual(r_list.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(r_view.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        user = User.objects.get(email='hello@example.com')
        user.delete()
