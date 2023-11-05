from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "tickets"

urlpatterns = [
    path("", views.home, name="index"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("leaderboard/", views.leaderboard, name="leaderboard")
    # path('profile/id/<int:user_id>/', views.profile, name='profile'),
]

