from django.db import models
import logging
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from movie.models import Movie

logger = logging.getLogger(__name__)


class UserReviewManager(models.Manager):
    def add_review(self, movie_obj, user_obj, review: str):
        try:
            data, status_code = self.create(movie=movie_obj, user=user_obj, user_review=review)
            return data, status.HTTP_200_OK

        except Exception as e:
            logger.exception(str(e))
            return None, status.HTTP_500_INTERNAL_SERVER_ERROR

    @staticmethod
    def get_movie(title: str):
        try:
            data = Movie.objects.get(title=title)
            return data, status.HTTP_200_OK

        except ObjectDoesNotExist:
            return None, status.HTTP_404_NOT_FOUND

        except Exception as e:
            logger.exception(str(e))
            return None, status.HTTP_500_INTERNAL_SERVER_ERROR

    def get_review(self, movie):
        try:
            data = self.get(movie=movie)
            return data, status.HTTP_200_OK

        except ObjectDoesNotExist:
            return None, status.HTTP_404_NOT_FOUND

        except Exception as e:
            logger.exception(str(e))
            return None, status.HTTP_500_INTERNAL_SERVER_ERROR

    def delete_review(self, movie) -> (tuple, int):
        try:
            data = self.get(movie=movie).delete()
            return data, status.HTTP_200_OK

        except ObjectDoesNotExist:
            return None, status.HTTP_404_NOT_FOUND

        except Exception as e:
            logger.exception(str(e))
            return None, status.HTTP_500_INTERNAL_SERVER_ERROR



