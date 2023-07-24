from django.urls import path
from .views import AddMovieView, DeleteMovieView, GetMovieListView

urlpatterns = [
    path('add/movie/', AddMovieView.as_view(), name='add_movie'),
    path('get/movie/list', GetMovieListView.as_view(), name='get_movie_list'),
    # path('update/movie/', ),
    path('delete/movie/', DeleteMovieView.as_view(), name='delete_movie'),
]


