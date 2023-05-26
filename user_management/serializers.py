from rest_framework import serializers


class User(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    first_name = models.CharField(max_length=250, required=False)
    last_name = models.CharField(max_length=250,  required=False)
    username = models.CharField(min_length=4, max_length=50,  required=True)
    email = models.CharField(max_length=250, required=True)
    