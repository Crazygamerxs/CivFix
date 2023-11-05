from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "tickets"

urlpatterns = [
    path("", views.home, name="index"),
    path("home/", views.home, name="home"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("profile/", views.profile, name="profile"),
    # path('profile/id/<int:user_id>/', views.profile, name='profile'),
]

