from django.contrib import admin
from .models import Ticket, Upvote

admin.site.register(Ticket)
admin.site.register(Upvote)

# from django.contrib import admin

# from .models import UserProfile

# # Register your models here.
# admin.site.register(UserProfile)
