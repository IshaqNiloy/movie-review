from applibs import response_helper, response_messages
from rest_framework.views import APIView
from .models import UserReview
from .serializers import (
    AddUserReviewSerializer,
)


class AddUserReview(APIView):
    def __init__(self):
        super(AddUserReview, self).__init__()
        self.request_data = None
        self.serializer = AddUserReviewSerializer
        self.model = UserReview
        self.lang = 'en'

    def get_movie_data(self, title: str):
        return self.model.objects.get_movie(title)

    def add_user_review(self, movie_obj, user_review: str):
        return self.model.objects.add_review(movie_obj, user_review)

    def post(self, request):
        try:
            self.request_data = request.data
            self.serializer = self.serializer(data=self.request_data)
            self.lang = request.headers.get('lang', 'en')

            if self.serializer.is_valid():
                movie_title = self.serializer.validated_data['title']
                movie_obj = self.get_movie_data(movie_title)

                if not movie_obj:
                    return response_helper.error_response(message=response_messages.MOVIE_DOES_NOT_EXIST,
                                                          lang=self.lang)

                # add movie review
                user_review_obj = self.add_user_review(movie_obj, self.serializer.validated_data['user_review'])

                if user_review_obj:
                    return response_helper.success_response(message=response_messages.USER_REVIEW_SAVE_SUCCESS,
                                                            lang=self.lang)
                else:
                    return response_helper.error_response(message=response_messages.USER_REVIEW_SAVE_FAILED,
                                                          lang=self.lang)

            else:
                return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA, lang=self.lang)

        except Exception as e:
            return response_helper.error_response(message=response_messages.USER_REVIEW_SAVE_FAILED, lang=self.lang,
                                                  details=str(e))


class GetUserReview:
    pass


class UpdateUserReview:
    pass


class DeleteUserReview:
    pass
