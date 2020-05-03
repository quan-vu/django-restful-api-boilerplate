from django.urls import include, path, reverse
from rest_framework import status, routers
from rest_framework.test import APITestCase, APIClient, URLPatternsTestCase
from core.models import User
from posts.models import Post


class PostTests(APITestCase):

    def setUp(self):

        # Group: Authors
        # Can: Add, Change, Delete, Hide, View the post
        
        self.user_normal = User.objects.create_user(
            username="tom", 
            password="T0m@Cat",
            email="tom@example.com",
        )

        # Login as User normal
        url = 'http://localhost:8000/api/auth/token/'
        self.user_normal_login = {
            'username': 'tom',
            'password': 'T0m@Cat'
        }
        response = self.client.post(url, data=self.user_normal_login, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)
        self.user_normal_token = response.data['access']

    def test_non_authors_cannot_create_post(self):
        url = 'http://localhost:8000/api/posts/'

        # Step 1: Authentication with token 
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_normal_token) 

        # Step 2: Create a post
        post_1 = {
            "title": "Post 1",
            "slug": "post-1",
            "content": "Tom create this post"
        }
        response = client.post(url, post_1, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)