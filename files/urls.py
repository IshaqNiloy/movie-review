from django.urls import path
from .views import FileUploadView
from movie_review import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file_upload_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MOVIE_MEDIA_URL, document_root=settings.MEDIA_ROOT)
