from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import MovieSerializer
from .models import Movie
from applibs import response_helper
# Create your views here.


class AddMovieView(APIView):
    def __init__(self):
        super(AddMovieView, self).__init__()
        self.request_data = None
        self.serializer = MovieSerializer
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

                if data is not None:
                    return response_helper.success_response(message="Movie saved successfully!")
                else:
                    return response_helper.error_response(message="Movie not saved!")
            else:
                return response_helper.error_response(message="Invalid request data!")

        except:
            pass