from django.db import models


class MovieManager(models.Manager):
    def add_movie(self, title, rating, director, writer, stars, storyline, genres, release_date, countries_of_origin, language,
                  filming_locations, production_companies, budget, gross_worldwide, runtime):

        data = self.create(title=title, rating=rating, director=director, writer=writer, stars=stars, storyline=storyline, genres=genres, release_date=release_date,
                            countries_of_origin=countries_of_origin, language=language, filming_locations=filming_locations, production_companies=production_companies,
                           budget=budget, gross_worldwide=gross_worldwide, runtime=runtime)

        return data



