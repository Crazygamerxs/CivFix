from django.contrib import admin
from django.urls import path, include

# import users model
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
    path('tickets/', include('tickets.urls')),
]



