"""
python manage.py runscript scripts.movie_onboard.movie_bulk_onboard
"""
import time

import pandas as pd
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from files.models import Files
from movie.models import Movie
from files.choices import FileStatus
import logging

logger = logging.getLogger(__name__)


def run():
    logger.info('movie bulk onboard start running...')
    script_start_time = time.time()
    try:
        with transaction.atomic():
            file_objects = Files.objects.filter(status=FileStatus.PENDING)

            if len(file_objects) > 0:
                file_data_df = pd.DataFrame()
                for file_object in file_objects:
                    file_data_df = pd.concat([file_data_df, pd.read_csv(file_object.file)], axis=0)

                movie_records = file_data_df.to_dict(orient='records')
                movie_object_list = []

                for record in movie_records:
                    title = record['title']
                    rating = record['rating']
                    director = record['director']
                    writer = record['writer']
                    stars = record['stars']
                    storyline = record['storyline']
                    genres = record['genres']
                    release_date = record['release_date']
                    countries_of_origin = record['countries_of_origin']
                    language = record['language']
                    filming_locations = record['filming_locations']
                    production_companies = record['production_companies']
                    budget = record['budget']
                    gross_worldwide = record['gross_worldwide']
                    runtime = record['runtime']

                    movie_object = Movie(title=title, rating=rating, director=director, writer=writer,
                                         stars=stars, storyline=storyline, genres=genres,
                                         release_date=release_date, countries_of_origin=countries_of_origin,
                                         language=language, filming_locations=filming_locations,
                                         production_companies=production_companies, budget=budget,
                                         gross_worldwide=gross_worldwide, runtime=runtime)

                    movie_object_list.append(movie_object)

                Movie.objects.bulk_create(movie_object_list)
                file_objects.update(status=FileStatus.SYNCED)

            synced = len(Files.objects.filter(status='Synced'))
            pending = len(Files.objects.filter(status='Pending'))
            failed = len(Files.objects.filter(status='Failed'))

            logger.info(f'Synced: {synced} Pending: {pending} Failed: {failed}')

    except ObjectDoesNotExist as e:
        file_objects.update(status=FileStatus.FAILED)
        logger.error(str(e))

    except Exception as e:
        file_objects.update(status=FileStatus.FAILED)
        logger.error(str(e))

    script_end_time = int((time.time() - script_start_time) * 1000)
    logger.info(f"Execution time {script_end_time} ms")



