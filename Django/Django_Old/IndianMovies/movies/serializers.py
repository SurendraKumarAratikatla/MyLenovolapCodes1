from rest_framework import serializers
from .models import MoviesList

class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesList
        fields = ('id','name')


