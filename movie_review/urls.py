from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/review/', include('movie.urls')),
    path('movie/review/user/', include('user_management.urls')),
    path('movie/review/file/', include('files.urls')),
    path('movie/review/user-review/', include('user_review.urls')),
    path('movie/review/api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
