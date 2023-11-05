from django.contrib import admin
from .models import Ticket, Upvote, Profile

admin.site.register(Ticket)
admin.site.register(Upvote)
admin.site.register(Profile)
