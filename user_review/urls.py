from django.urls import path
from .views import (
    AddUserReview,
    GetUserReview,
    UpdateUserReview,
    DeleteUserReview
)

urlpatterns = [
    path('add', AddUserReview.as_view(), name='add_review'),
    # path('get', GetUserReview.as_view(), name='get_review'),
    # path('update', UpdateUserReview.as_view(), name='update_review'),
    # path('delete', DeleteUserReview.as_view(), name='delete_review'),
]
