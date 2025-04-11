from django.db import models
from django.conf import settings
# Create your models here.
class Movie(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    score = models.FloatField()


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)