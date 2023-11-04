from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('home/', views.home, name='home'),
]


