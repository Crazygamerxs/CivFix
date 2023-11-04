from django.contrib import admin
from django.urls import path, include
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('tickets/', include('tickets.urls', namespace='tickets')),
    # path('', views.index, name='home')
]



