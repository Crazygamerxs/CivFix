from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),    
]


# urlpatterns = [
#     # user profile page
#     path('id/<int:user_id>/', views.profile, name='profile'),
#     path('leaderboard/', views.leaderboard, name='leaderboard'),
# ]

# from django.contrib import admin
# from django.urls import path
# from . import views

# app_name = 'tickets'

# urlpatterns = [
#     path('home/', views.home, name='home'),
# ]


