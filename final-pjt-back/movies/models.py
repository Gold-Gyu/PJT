from django.db import models
from django.conf import settings
# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    # actors = models.ManyToManyField(Actor, related_name="movies")
    title = models.CharField(max_length=100)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    poster_path = models.TextField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    genre_ids = models.ManyToManyField(Genre, related_name='movies')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movie', blank=True)
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # like_users =models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_reviews")
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


