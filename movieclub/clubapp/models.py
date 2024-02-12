from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    movie_title = models.CharField(max_length=255)
    added_by_users = models.ManyToManyField(User, related_name='movies')

    def __str__(self):
        return self.movie_title