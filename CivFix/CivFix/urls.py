from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('tickets/', include('tickets.urls', namespace='tickets')),
    path('', views.index, name='index'),
    # path('users/', include('users.urls', namespace='users')),
    path('tickets/', include('tickets.urls')),
]



