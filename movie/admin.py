from django.contrib import admin
from movie import models
# Register your models here.


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'director', 'writer', 'stars', 'storyline', 'genres', 'release_date', 'countries_of_origin', 'language', 'filming_locations', 'production_companies',
                    'budget', 'gross_worldwide', 'runtime', 'created_at', 'updated_at']
    list_filter = ['rating', 'director', 'writer', 'genres', 'language',]
    search_fields = ['title', 'director', 'writer', 'stars', 'language']
