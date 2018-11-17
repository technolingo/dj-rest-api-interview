from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework.authtoken.models import Token

from ..models import User

from datetime import date


class UserAPITestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(
            email='hello@example.com',
            birthday=date.today(),
            membership_status='0'
        )
        user.set_password('simpleSecret123')
        user.save()

    def test_obtain_token_api_fail(self):
        url = api_reverse('api:obtain_token')
        data = {
            'email': 'hello@exam11ple.com',
            'password': 'wrongPass456778'
        }
        r = self.client.post(url, data, format='json')
        token = r.data.get('token', None)

        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNone(token)

    def test_obtain_token_api_success(self):
        url = api_reverse('api:obtain_token')
        data = {
            'email': 'hello@example.com',
            'password': 'simpleSecret123'
        }
        r = self.client.post(url, data, format='json')
        token = r.data.get('token', None)

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(token)

    def test_token_authentication_fail(self):
        url = api_reverse('api:my_profile')
        r = self.client.get(url, format='json')

        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_authentication_success(self):
        token = Token.objects.get(user__email='hello@example.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = api_reverse('api:my_profile')
        r = self.client.get(url, format='json')

        self.assertIsNotNone(token)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
