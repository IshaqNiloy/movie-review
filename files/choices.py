from django.db import models
from django.utils.translation import gettext_lazy as _


class FileStatus(models.TextChoices):
    PENDING = 'Pending', _('Pending')
    SYNCED = 'Synced', _('Synced')
    FAILED = 'Failed', _('Failed')
