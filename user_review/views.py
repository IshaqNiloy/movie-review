import logging

from applibs import response_helper, response_messages
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserReview
from .serializers import (
    AddUserReviewSerializer,
    GetUserReviewSerializer,
    DeleteUserReviewSerializer
)


class Base(APIView):
    def __init__(self):
        super(Base, self).__init__()
        self.model = UserReview
        self.request_data = None
        self.lang = 'en'

    def get_movie_data(self, title: str):
        return self.model.objects.get_movie(title=title)

    def get_user_review(self, user, movie) -> ():
        return self.model.objects.get_review(user=user, movie=movie)


class AddUserReview(Base):
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(AddUserReview, self).__init__()
        self.serializer = AddUserReviewSerializer

    def add_user_review(self, movie_obj, user_obj, user_review: str):
        return self.model.objects.add_review(movie_obj, user_obj, user_review)

    def post(self, request):
        try:
            self.request_data = request.data
            self.serializer = self.serializer(data=self.request_data)
            self.lang = request.headers.get('lang', 'en')

            if self.serializer.is_valid():
                movie_title = self.serializer.validated_data['title']
                movie_obj, res_status = self.get_movie_data(movie_title)

                if res_status != status.HTTP_200_OK:
                    return response_helper.error_response(message=response_messages.MOVIE_DATA_FETCH_FAILED,
                                                          lang=self.lang)

                # add movie review
                user_review_obj, res_status = self.add_user_review(movie_obj=movie_obj, user_obj=self.request.user,
                                                                   user_review=self.serializer.validated_data['user_review'])

                if res_status == status.HTTP_409_CONFLICT:
                    return response_helper.error_response(message=response_messages.USER_REVIEW_ALREADY_EXIST,
                                                          lang=self.lang)

                if res_status != status.HTTP_200_OK:
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
        self.request_data = None
        self.serializer = GetUserReviewSerializer
        self.lang = None

    def post(self, request):
        try:
            self.request_data = request.data
            self.lang = request.headers.get('Accept-Language', 'en')
            self.serializer = self.serializer(data=self.request_data)

            if self.serializer.is_valid():
                # movie title
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



class UpdateUserReview:
    pass


class DeleteUserReview(Base):
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(DeleteUserReview, self).__init__()
        self.serializer = DeleteUserReviewSerializer

    def delete_user_review(self, movie: str) -> (tuple, int):
        return self.model.objects.delete_review(movie=movie)

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
