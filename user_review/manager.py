from django.db import models
from movie.models import Movie
import logging

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


