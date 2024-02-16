from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    movie_title = models.CharField(max_length=255)
    movie_overview = models.CharField(max_length=255, null=True)
    movie_poster_path = models.CharField(max_length=255, null=True)
    movie_release_date = models.CharField(max_length=255, null=True)
    movie_vote_average = models.FloatField(null=True, blank=True)
    added_by_users = models.ManyToManyField(User, related_name='movies')

    def __str__(self):
        return self.movie_title