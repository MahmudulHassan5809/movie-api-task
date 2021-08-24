from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from movies.models import Movie
from movies.serializers import MovieSerializer
from django.urls import reverse,reverse_lazy

# Create your tests here.

MOVIES_URL = reverse('movies:movie-list')
COMMENTS_URL = reverse('movies:comment-list')

class PublicMovieAPITest(TestCase):
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
    

    def test_retrieve_movies(self):
        res = self.client.get(MOVIES_URL)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
    
    def test_movie_already_exists(self):
        payload_1 = {
            'title' : 'Test Movie',
        }
        res_1 = self.client.post(MOVIES_URL,payload_1)
        res_2 = self.client.post(MOVIES_URL,payload_1)
        self.assertEqual(res_2.status_code,status.HTTP_400_BAD_REQUEST)
        
        
class PublicCommentApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_comment_create_test_by_valid_data(self):
        movie_obj = Movie.objects.create(title='Test Movie Again')
        payload = {
            'movie' : movie_obj.id,
            'comment' : 'Test Comment'
        }
        res = self.client.post(COMMENTS_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)

    
    def test_comment_create_test_by_invalid_data_only_movie(self):
        movie_obj = Movie.objects.create(title='Test Movie Again')
        payload = {
            'movie' : movie_obj.id,
        }
        res = self.client.post(COMMENTS_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
    
    def test_comment_create_test_by_invalid_data_only_body(self):
        movie_obj = Movie.objects.create(title='Test Movie Again')
        payload = {
            'comment' : 'ghgh',
        }
        res = self.client.post(COMMENTS_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
