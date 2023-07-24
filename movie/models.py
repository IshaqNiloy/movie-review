from django.db import models
from django.utils import timezone
from movie.manager import MovieManager

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=250, blank=False)
    rating = models.DecimalField(decimal_places=1, max_digits=2, blank=False)
    director = models.CharField(max_length=250, blank=False)
    writer = models.CharField(max_length=250, blank=False)
    stars = models.CharField(max_length=250, blank=False)
    storyline = models.TextField(blank=False)
    genres = models.CharField(max_length=250, blank=False)
    release_date = models.DateField(blank=True, null=True)
    countries_of_origin = models.CharField(max_length=250, blank=True, null=True)
    language = models.CharField(max_length=250, blank=False)
    filming_locations = models.CharField(max_length=250, blank=False)
    production_companies = models.CharField(max_length=250, blank=False)
    budget = models.IntegerField(blank=False)
    gross_worldwide = models.IntegerField(blank=False)
    runtime = models.IntegerField(blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    objects = MovieManager()

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
