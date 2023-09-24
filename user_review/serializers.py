from rest_framework import serializers


class AddUserReviewSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    title = serializers.CharField(max_length=250, required=True)
    user_review = serializers.CharField(required=True)


class GetUserReviewSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class DeleteUserReviewSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    title = serializers.CharField(max_length=250, required=True)
