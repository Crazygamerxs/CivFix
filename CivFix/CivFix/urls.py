from django.contrib import admin
from django.urls import path, include

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('tickets/', include('tickets.urls', namespace='tickets')),
    # path('', views.index, name='index'),
<<<<<<< HEAD
=======
    path("", views.index, name="index"),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
>>>>>>> f6471237a326944eb024bd8b1413791b52a229de
    # path('tickets/', include('tickets.urls')),
    
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


