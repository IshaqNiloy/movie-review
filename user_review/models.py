from django.db import models
from movie.models import Movie
from .manager import UserReviewManager


# Create your models here.

class UserReview(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_review = models.TextField(null=False, blank=False)

    objects = UserReviewManager()

    class Meta:
        verbose_name = 'user review'
        verbose_name_plural = 'user reviews'

    def __str__(self):
        return self.movie.title
