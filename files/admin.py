from django.contrib import admin
from .models import Files


@admin.register(Files)
class FileAdmin(admin.ModelAdmin):
    list_display = ['file', 'status', 'created_at', 'updated_at']
    search_fields = ['file', 'status']
    list_filter = ['status']
