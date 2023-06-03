from django.db import models
from django.utils import timezone
from .choices import FileStatus
from .manager import FilesManager


class Files(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    file = models.FileField(blank=False, null=False)
    status = models.CharField(max_length=50, choices=FileStatus.choices, default=FileStatus.PENDING, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    objects = FilesManager()

    class Meta:
        verbose_name = 'file'
        verbose_name_plural = 'files'

    def __str__(self):
        return self.file
