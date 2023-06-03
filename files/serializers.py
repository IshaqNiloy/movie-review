from rest_framework import serializers


class FileUploadViewSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    file = serializers.FileField(required=True)
