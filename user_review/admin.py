from django.contrib import admin
from .models import UserReview
# Register your models here.


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'user_review']
    search_fields = ['movie', 'user']
    list_filter = ['movie', 'user']


