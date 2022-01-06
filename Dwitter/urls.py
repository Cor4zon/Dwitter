from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include("social.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("users/", include("users.urls")),
    path('admin/', admin.site.urls),
]
