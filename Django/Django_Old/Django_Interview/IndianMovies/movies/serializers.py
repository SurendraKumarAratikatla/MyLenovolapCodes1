from rest_framework import serializers
from .models import MoviesList

class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesList
        fields = ('movie_name','hero_name','heroin_name','music_director_name','director_name')


