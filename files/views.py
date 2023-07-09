import os

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .serializers import FileUploadViewSerializer
from icecream import ic
from applibs import response_helper, response_messages
from .models import Files


class FileUploadView(APIView):
    permission_classes = [IsAdminUser]

    def __init__(self):
        super(FileUploadView, self).__init__()
        self.request_data = None
        self.serializer = FileUploadViewSerializer
        self.model = Files
        self.args = None
        self.kwargs = None

    def post(self, request):
        try:
            self.request_data = request.data
            self.serializer = self.serializer(data=self.request_data)
            try:
                if self.serializer.is_valid():
                    validated_file = self.serializer.validated_data.get('file')
                    # Checking for csv file
                    if validated_file.name[-3:] != 'csv':
                        return response_helper.error_response(message=response_messages.ONLY_ACCEPT_CSV)

                    db_file_path = self.model.objects.values_list('file', flat=True)
                    ic(db_file_path)

                    # Checking for duplicate file name
                    if (os.getenv('MOVIE_MEDIA_URL') + validated_file.name) in db_file_path:
                        return response_helper.error_response(message=response_messages.DUPLICATE_FILE_NAME)

                    file = self.model.objects.upload_file(file=validated_file)

                    response_data = {
                        "file": validated_file.name,
                        "status": file.status
                    }

                    return response_helper.success_response(message=response_messages.FILE_UPLOAD_SUCCESS,
                                                            data=response_data)
                else:
                    return response_helper.error_response(message=response_messages.INVALID_REQUEST_DATA)

            except Exception as e:
                return response_helper.error_response(message=response_messages.FILE_UPLOAD_FAILED, details=str(e))

        except Exception as e:
            return response_helper.error_response(message=response_messages.FILE_UPLOAD_FAILED, details=str(e))

