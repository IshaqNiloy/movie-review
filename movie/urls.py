from django.urls import path
from .views import AddMovieView

urlpatterns = [
    path('add/movie/', AddMovieView.as_view(), name='add_movie'),
    # path('get/movie/', ),
    # path('update/movie/', ),
    # path('delete/movie/', ),
]