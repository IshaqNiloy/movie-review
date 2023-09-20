from django.db import models
from movie.models import Movie
from user_management.models import User
from .manager import UserReviewManager


# Create your models here.

class UserReview(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    user_review = models.TextField(null=False, blank=False)

    objects = UserReviewManager()

    class Meta:
        unique_together = ('movie', 'user')
        verbose_name = 'user review'
        verbose_name_plural = 'user reviews'

    def __str__(self):
        return self.movie.title
