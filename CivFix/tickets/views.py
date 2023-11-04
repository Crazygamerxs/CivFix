from django.shortcuts import render
from .models import Ticket, Upvote


def home(request):
    tickets = Ticket.objects.all()  # Retrieve all tickets from the database.
    upvotes = Upvote.objects.all()
    return render(request, 'tickets/home.html', {'tickets': tickets, 'upvotes': upvotes})
