from rest_framework import serializers
from movies.models import Movie,Comment
from rest_framework import serializers



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class MovieAddSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


