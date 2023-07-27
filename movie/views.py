from django.shortcuts import render
from rest_framework.views import APIView
from .models import Movie
from applibs import response_helper, response_messages
from .serializers import (
    AddMovieSerializer,
    DeleteMovieSerializer,
    GetMovieListSerializer,
    UpdateMovieSerializer,
)


class AddMovieView(APIView):
    def __init__(self):
        super(AddMovieView, self).__init__()
        self.request_data = None
        self.serializer = AddMovieSerializer
        self.args = None
        self.kwargs = None

    def post(self, request, *args, **kwargs):
        try:
            self.request_data = request.data
            self.serializer = self.serializer(data=self.request_data)

            if self.serializer.is_valid():
                title = self.serializer.validated_data.get('title')
                rating = self.serializer.validated_data.get('rating')
                director = self.serializer.validated_data.get('director')
                writer = self.serializer.validated_data.get('writer')
                stars = self.serializer.validated_data.get('stars')
                storyline = self.serializer.validated_data.get('storyline')
                genres = self.serializer.validated_data.get('genres')
                release_date = self.serializer.validated_data.get('release_date')
                countries_of_origin = self.serializer.validated_data.get('countries_of_origin')
                language = self.serializer.validated_data.get('language')
                filming_locations = self.serializer.validated_data.get('filming_locations')
                production_companies = self.serializer.validated_data.get('production_companies')
                budget = self.serializer.validated_data.get('budget')
                gross_worldwide = self.serializer.validated_data.get('gross_worldwide')
                runtime = self.serializer.validated_data.get('runtime')

                data = Movie.objects.add_movie(title, rating, director, writer, stars, storyline, genres, release_date, countries_of_origin, language,
                                                 filming_locations, production_companies, budget, gross_worldwide, runtime)

                return response_helper.success_response(message=response_messages.MOVIE_SAVE_SUCCESS, data=str(data))

            else:
                return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA)

        except Exception as e:
            return response_helper.error_response(message=response_messages.MOVIE_SAVE_FAILED, details=str(e))


class GetMovieListView(APIView):
    def __init__(self):
        super(GetMovieListView, self).__init__()
        self.request_data = None
        self.serializer = GetMovieListSerializer
        self.args = None
        self.kwargs = None

    def get(self, request, *args, **kwargs):
        try:
            data = Movie.objects.get_movie_list()
            movie_list = [movie for movie in data]

            return response_helper.success_response(message=response_messages.MOVIE_LIST_FETCH_SUCCESS,
                                                    data=movie_list)

        except Exception as e:
            return response_helper.error_response(message=response_messages.MOVIE_LIST_FETCH_FAILED, details=str(e))


class UpdateMovieView(APIView):
    def __init__(self):
        super(UpdateMovieView, self).__init__()
        self.request_data = None
        self.serializer = UpdateMovieSerializer
        self.args = None
        self.kwargs = None

    def post(self, request, *args, **kwargs):
        try:
            self.request_data = request.data
            self.serializer = self.serializer(data=self.request_data)

            if self.serializer.is_valid():
                movie = Movie.objects.filter(title=self.request_data['title'])

                for key in self.request_data.keys():
                    updated_movie = movie.update(key=self.request_data[key])
                return response_helper.success_response(message=response_messages.MOVIE_UPDATE_SUCCESS,
                                                        data=updated_movie)
            else:
                return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA)

        except Exception as e:
            return response_helper.success_response(message=response_messages.MOVIE_UPDATE_FAILED, details=str(e))
                

class DeleteMovieView(APIView):
    def __init__(self):
        super(DeleteMovieView, self).__init__()
        self.request_data = None
        self.serializer = DeleteMovieSerializer
        self.args = None
        self.kwargs = None

    def post(self, request, *args, **kwargs):
        try:
            self.request_data = request.data
            self.serializer = self.serializer(data=self.request_data)

            if self.serializer.is_valid():
                title = self.serializer.validated_data.get('title')

                data = Movie.objects.delete_movie(title)

                return response_helper.success_response(message=response_messages.MOVIE_DELETE_SUCCESS, data=data)
            else:

                return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA)

        except Exception as e:
            return response_helper.error_response(message=response_messages.MOVIE_DELETE_FAILED, details=str(e))