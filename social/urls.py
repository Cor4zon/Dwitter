from django.urls import path
from social import views

app_name = "social"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("profiles/", views.profiles, name="profiles"),
    path("profile/<int:pk>", views.profile, name="profile"),
]