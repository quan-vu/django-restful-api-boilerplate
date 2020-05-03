from django.urls import include, path, reverse
from rest_framework import status, routers
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from core.models import User


class UserTests(APITestCase):

    def setUp(self):
        self.user_tom = User.objects.create_user(
            username="johnsmith", 
            email="johnsmith@example.com",
            password="j#1thing"
        )
        self.base_url = 'http://localhost:8000'
        self.endpoints = {
            'auth_token': self.base_url + '/api/auth/token/',
            'posts':self.base_url + '/api/posts/'
        }

    def test_create_user(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('user-list')
        data = {
            'username': 'johnsmith2',
            'email': 'johnsmith2@example.com',
            'password': 'j#1thing'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])

    def test_login_and_get_auth_token(self):
        data = {
            'username': 'johnsmith',
            'password': 'j#1thing'
        }
        response = self.client.post(self.endpoints['auth_token'], data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
        self.token = response.data['access']

    def test_GET_posts_resource_with_token(self):
        # Login to get access token
        self.test_login_and_get_auth_token()   

        # Step 1: Authentication with token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Step 2: Get list of Posts resource
        response = self.client.get(self.endpoints['posts'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_GET_posts_resource_without_token(self):
        # Step 2: Get list of Posts resource
        response = self.client.get(self.endpoints['posts'])
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)