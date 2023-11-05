from django.urls import path
from . import views

urlpatterns = [
    path('id/<int:user_id>/', views.profile, name='profile'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
