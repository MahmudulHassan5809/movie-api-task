from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.renderers import JSONRenderer

from movies.models import Movie,Comment
from movies.serializers import MovieSerializer,CommentSerializer,MovieAddSerializer

from utils.movie_api import get_movie_data_by_title
from utils.helper_func import format_movie_data
from utils.herler_class import OnlyRawBrowsableAPIRenderer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['get','post']
    search_fields = ['$title','$plot','$actors']
    ordering_fields = ['imdb_rating']
    
    def get_queryset(self):
        fields = self.request.GET.copy()
        qs = self.queryset
        
        try:
            fields.pop('search')
        except KeyError:
            pass
        
        qs = qs.filter_by_query(fields.dict())
        return qs

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'create':
            return MovieAddSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        add_serializer = MovieAddSerializer(data = request.data)
        add_serializer.is_valid(raise_exception=True)

        title = add_serializer.data.get('title') or None
        
        data = get_movie_data_by_title(title)

        if data['status'] == 200:
            data = data['result']
            data.pop('Response')
            data = format_movie_data(data)
            serializer = MovieSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'detail' : data['msg']},status=data['status'])


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    renderer_classes = [OnlyRawBrowsableAPIRenderer, JSONRenderer]
    http_method_names = ['get','post']

    def get_queryset(self):
        fields = self.request.GET.copy()
        qs = self.queryset
        
        try:
            fields.pop('search')
        except KeyError:
            pass
        
        qs = qs.filter_by_query(fields.dict())
        return qs

    

