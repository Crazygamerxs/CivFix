from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("tickets/", include("tickets.urls")),
    path("admin/", admin.site.urls),
]

