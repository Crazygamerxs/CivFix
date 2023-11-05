from django.contrib import admin
from .models import Ticket, Upvote, UserProfile

admin.site.register(Ticket)
admin.site.register(Upvote)
admin.site.register(UserProfile)
