from rest_framework import serializers
from applibs import response_helper, response_messages


class FileUploadViewSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    # def perform_validation(self, data):
    #     try:
    #         validated_data = super().perform_validation(data)
    #     except serializers.ValidationError as e:
    #         raise serializers.ValidationError("Error message") from e

    file = serializers.FileField(required=True)

    def validate_file_field(self, value):
        if not value:
            raise serializers.ValidationError("File field is required.")

        return value
