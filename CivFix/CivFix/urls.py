from django.contrib import admin
from django.urls import path, include
from . import views


from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('tickets/', include('tickets.urls', namespace='tickets')),
    # path('', views.index, name='index'),
    # path('tickets/', include('tickets.urls')),
    
]


# urlpatterns = [
#     # user profile page
#     path('id/<int:user_id>/', views.profile, name='profile'),
#     path('leaderboard/', views.leaderboard, name='leaderboard'),
# ]

