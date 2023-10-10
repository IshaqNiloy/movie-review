from django.db import models
import logging
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from movie.models import Movie

logger = logging.getLogger(__name__)


class UserReviewManager(models.Manager):
    def add_review(self, movie_obj, user_obj, review: str):
        return self.create(movie=movie_obj, user=user_obj, user_review=review)

    @staticmethod
    def get_movie(title: str):
        return Movie.objects.filter(title=title).last()

    def get_review(self, user, movie):
        return self.filter(movie=movie, user=user).last()

    def delete_review(self, movie):
        return self.filter(movie=movie).last().delete()




