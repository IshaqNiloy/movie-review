import logging

from applibs import response_helper, response_messages
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserReview
from .serializers import (
    AddUserReviewSerializer,
    GetUserReviewSerializer,
    DeleteUserReviewSerializer,
    UpdateUserReviewSerializer
)


class Base(APIView):
    def __init__(self):
        super(Base, self).__init__()
        self.model = UserReview
        self.request_data = None
        self.lang = 'en'

    def get_movie_data(self, title: str):
        return self.model.objects.get_movie(title=title)

    def get_user_review(self, user, movie):
        return self.model.objects.get_review(user=user, movie_obj=movie)


class AddUserReview(Base):
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(AddUserReview, self).__init__()
        self.serializer = AddUserReviewSerializer

    def add_user_review(self, movie, user, user_review: str):
        return self.model.objects.add_review(movie=movie, user=user, review=user_review)

    def post(self, request):
        try:
            self.request_data = request.data
            self.serializer = self.serializer(data=self.request_data)
            self.lang = request.headers.get('lang', 'en')

            if self.serializer.is_valid():
                movie_title = self.serializer.validated_data['title']
                user_review = self.serializer.validated_data['user_review']

                # get movie
                movie_obj = self.get_movie_data(movie_title)

                if not movie_obj:
                    return response_helper.error_response(message=response_messages.MOVIE_DATA_FETCH_FAILED,
                                                          lang=self.lang)

                # add movie review
                user_review_obj = self.add_user_review(movie=movie_obj, user=request.user, user_review=user_review)

                if not user_review_obj:
                    return response_helper.error_response(message=response_messages.USER_REVIEW_SAVE_FAILED,
                                                          lang=self.lang)

                return response_helper.success_response(message=response_messages.USER_REVIEW_SAVE_SUCCESS,
                                                        lang=self.lang)

            else:
                return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA, lang=self.lang)

        except Exception as e:
            return response_helper.error_response(message=response_messages.USER_REVIEW_SAVE_FAILED, lang=self.lang,
                                                  details=str(e))


class GetUserReview(Base):
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(GetUserReview, self).__init__()
        self.serializer = GetUserReviewSerializer

    def post(self, request):
        try:
            self.request_data = request.data
            self.lang = request.headers.get('Accept-Language', 'en')
            self.serializer = self.serializer(data=self.request_data)

            if self.serializer.is_valid():
                movie_title = self.serializer.validated_data['title']

                # get movie
                movie_obj = self.get_movie_data(title=movie_title)

                if not movie_obj:
                    return response_helper.error_response(message=response_messages.MOVIE_DATA_FETCH_FAILED,
                                                          lang=self.lang)
                # get review
                movie_review = self.get_user_review(user=request.user, movie=movie_obj)

                if not movie_review:
                    return response_helper.error_response(message=response_messages.USER_REVIEW_FETCH_FAILED,
                                                          lang=self.lang)

                # json response
                response = {
                    'title': movie_review.movie.title,
                    'review': movie_review.user_review
                }

                return response_helper.success_response(message=response_messages.USER_REVIEW_FETCH_SUCCESS,
                                                        data=response, lang=self.lang)

            else:
                return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA,
                                                      lang=self.lang)
        except Exception as e:
            return response_helper.error_response(message=response_messages.USER_REVIEW_FETCH_FAILED, details=str(e),
                                                  lang=self.lang)


class UpdateUserReview(Base):
    def __init__(self):
        super(UpdateUserReview, self).__init__()
        self.serializer = UpdateUserReviewSerializer

    @staticmethod
    def update_review_data(user, movie, review):
        return UserReview.objects.update_review(user, movie, review)

    def post(self, request):
        self.lang = request.headers.get('Accept-Language', 'en')
        self.request_data = request.data
        self.serializer = self.serializer(data=self.request_data)

        try:
            if self.serializer.is_valid():
                movie_title = self.serializer.validated_data.get('title')
                user_review = self.serializer.validated_data.get('user_review')

                # get movie
                movie_obj = self.get_movie_data(title=movie_title)

                if not movie_obj:
                    return response_helper.error_response(message=response_messages.MOVIE_DATA_FETCH_FAILED,
                                                          lang=self.lang)

                # update review
                self.update_review_data(user=request.user, movie=movie_obj, review=user_review)

        except Exception as e:
            return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA, lang=self.lang,
                                                  details=str(e))


class DeleteUserReview(Base):
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(DeleteUserReview, self).__init__()
        self.serializer = DeleteUserReviewSerializer

    def delete_user_review(self, movie: str) -> (tuple, int):
        return self.model.objects.delete_review(movie_obj=movie)

    def post(self, request):
        try:
            self.request_data = request.data
            self.serializer = self.serializer(data=self.request_data)

            if self.serializer.is_valid():
                # movie title
                movie_title = self.serializer.validated_data.get('title')

                # get movie
                movie_obj = self.get_movie_data(title=movie_title)

                if not movie_obj:
                    return response_helper.error_response(message=response_messages.MOVIE_DATA_FETCH_FAILED,
                                                          lang=self.lang)

                # get user review
                user_review = self.get_user_review(user=request.user, movie=movie_obj)

                if not user_review:
                    return response_helper.error_response(message=response_messages.USER_REVIEW_DELETE_FAILED,
                                                          lang=self.lang)

                # delete review
                self.delete_user_review(movie=movie_obj)

                return response_helper.error_response(message=response_messages.USER_REVIEW_DELETE_SUCCESS,
                                                      lang=self.lang)

            else:
                return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA, lang=self.lang)

        except Exception as e:
            return response_helper.error_response(message=response_messages.USER_REVIEW_DELETE_FAILED, lang=self.lang,
                                                  details=str(e))
