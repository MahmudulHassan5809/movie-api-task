from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse,reverse_lazy

# Create your tests here.

MOVIES_URL = reverse('movies:movie-list')

class PublicMovieCreateAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_movie_by_valid_title(self):
        payload = {
            'title' : 'Test Movie',
        }
        res = self.client.post(MOVIES_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
    
    def test_create_movie_by_invalid_title(self):
        payload = {
            'title' : '`&&&&Q&Q',
        }
        res = self.client.post(MOVIES_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_404_NOT_FOUND)

    def test_create_move_invalid(self):
        payload = {'title' : ''}
        res = self.client.post(MOVIES_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        

