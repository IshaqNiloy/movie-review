from rest_framework import serializers
from django.conf import settings


class MovieSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    title = serializers.CharField(min_length=1, max_length=250, required=True)
    rating = serializers.DecimalField(decimal_places=1, max_digits=2, required=True)
    director = serializers.ListField(min_length=1, max_length=10, required=True)
    writer = serializers.ListField(min_length=1, max_length=10, required=True)
    stars = serializers.ListField(min_length=1, max_length=10, required=True)
    storyline = serializers.CharField(min_length=1, required=True)
    genres = serializers.ListField(min_length=1, max_length=10, required=True)
    release_date = serializers.DateField(format(settings.DATE_INPUT_FORMATS), required=True)
    countries_of_origin = serializers.ListField(min_length=1, max_length=100, required=True)
    language = serializers.ListField(min_length=1, max_length=100, required=True)
    filming_locations = serializers.ListField(min_length=1, max_length=100, required=True)
    production_companies = serializers.ListField(min_length=1, max_length=100, required=True)
    budget = serializers.IntegerField(min_value=1, required=True)
    gross_worldwide = serializers.IntegerField(min_value=1, required=True)
    runtime = serializers.DurationField(min_value='00:01:00', required=True)


