from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TicketForm
from .models import Ticket, Upvote, Profile


def home(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = TicketForm()

    tickets = Ticket.objects.all()
    return render(request, 'home.html', {'tickets': tickets})


def profile(request, username):
    user = Profile.objects.get(user__username=username)
    return render(request, 'profile.html', {'user': user})


def leaderboard(request):
    leaderboard_users = Profile.objects.order_by('-points')[:10]  # Get top 10 users
    return render(request, 'leaderboard.html', {'leaderboard_users': leaderboard_users})