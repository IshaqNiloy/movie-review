from rest_framework import serializers


class UserViewSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    first_name = serializers.CharField(max_length=250, required=False)
    last_name = serializers.CharField(max_length=250,  required=False)
    username = serializers.CharField(min_length=4, max_length=50,  required=True)
    email = serializers.CharField(max_length=250, required=True)
    password = serializers.CharField(max_length=250, required=True)
    