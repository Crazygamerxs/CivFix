from django.urls import path
from . import views

urlpatterns = [
    # user profile page
    path('id/<int:user_id>/', views.profile, name='profile'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
