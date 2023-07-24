from django.contrib import admin
from user_management import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ['is_superuser', 'is_active', 'is_staff', 'is_admin']
    list_display = ['first_name', 'last_name', 'username', 'email', 'is_superuser', 'is_active', 'is_staff', 'is_admin', 'is_password_reset']
    search_fields = ['first_name', 'last_name', 'username', 'email']
