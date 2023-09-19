from django.db import models
from movie.models import Movie
import logging
from rest_framework import status

logger = logging.getLogger(__name__)


class UserReviewManager(models.Manager):
    def add_review(self, movie_obj, review: str):
        try:
            data = self.create(movie=movie_obj, user_review=review)
            return data

        except Exception as e:
            logger.exception(str(e))
            return None

    def get_movie(self, title: str):
        try:
            data = Movie.objects.get(title=title)
            return data

        except Exception as e:
            logger.exception(str(e))
            return None

    def get_user_review(self, movie):
        try:
          data = self.get(movie=movie)
          return data, status.HTTP_200_OK

        except Exception as e:
            logger.exception(str(e))

    def delete_review(self, movie) -> (tuple, int):
        try:
            data = self.filter(movie=movie).delete()
            return data, status.HTTP_200_OK

        except Exception as e:
            logger.exception(str(e))
            return None, status.



