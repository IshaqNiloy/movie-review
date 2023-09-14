from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/review/', include('movie.urls')),
    path('movie/review/user/', include('user_management.urls')),
    path('movie/review/file/', include('files.urls')),
    path('movie/review/user-review/', include('user_review.urls')),
]
