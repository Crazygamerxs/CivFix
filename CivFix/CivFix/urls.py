from django.contrib import admin
from django.urls import path, include
from . import views


from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('tickets/', include('tickets.urls', namespace='tickets')),
    # path('', views.index, name='index'),
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    # path('tickets/', include('tickets.urls')),
]
