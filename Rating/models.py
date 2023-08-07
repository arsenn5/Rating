from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Exercises(models.Model):
    title = models.CharField(max_length=100)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)


class ReviewRating(models.Model):
    rating = models.PositiveIntegerField()
    exercises = models.ForeignKey(Exercises, on_delete=models.CASCADE, related_name='reviews')
