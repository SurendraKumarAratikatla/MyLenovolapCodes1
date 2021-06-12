from django.db import models


class MoviesList(models.Model):
    movie_name = models.CharField(max_length=250)
    hero_name = models.CharField(max_length=550)
    heroin_name = models.CharField(max_length=100)
    music_director_name = models.CharField(max_length=1000)
    director_name = models.CharField(max_length=1000)
    def __str__(self):
        return self.movie_name + ' - ' + self.hero_name



class Songs(models.Model):
    album = models.ForeignKey(MoviesList, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=200)
