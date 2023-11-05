from django.urls import path
from . import views

app_name = "tickets"

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("profile/", views.profile, name="profile"),
    # URL pattern for upvoting
    path('upvote/<int:ticket_id>/', views.upvote_ticket, name='upvote_ticket'),
]