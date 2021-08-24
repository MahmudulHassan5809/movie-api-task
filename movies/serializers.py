from rest_framework import serializers
from movies.models import Movie,Comment
from rest_framework import serializers



class CommentSerializer(serializers.ModelSerializer):
    movie_name = serializers.SerializerMethodField()

    def get_movie_name(self,obj):
        return obj.movie.title
    class Meta:
        model = Comment
        fields = ['movie','comment','movie_name']



class MovieAddSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


