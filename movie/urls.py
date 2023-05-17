from django.urls import path
from .views import AddMovieView, DeleteMovieView

urlpatterns = [
    path('add/movie/', AddMovieView.as_view(), name='add_movie'),
    # path('get/movie/', ),
    # path('update/movie/', ),
    path('delete/movie/', DeleteMovieView.as_view(), name='delete_movie'),
]