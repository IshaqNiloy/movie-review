from django.db import models


class FilesManager(models.Manager):
    def upload_file(self, file):
        from .models import Files
        file_object = Files.objects.create(file=file)

        return file_object
