from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import TicketForm
from .models import Ticket, Upvote, Profile
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            admin_user = User.objects.get(username='admin')
            Ticket.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                location=form.cleaned_data['location'],
                status='OPEN',
                creator=admin_user
            )
            return redirect('tickets:home')
        else:
            print(form.errors)
            tickets = Ticket.objects.all().order_by('-created_at')
            return render(request, 'home.html', {'form': form, 'tickets': tickets})
    else:
        form = TicketForm()
        tickets = Ticket.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'form': form, 'tickets': tickets})


@csrf_exempt
@require_POST
def upvote_ticket(request, ticket_id):
    # Get the ticket object or return a 404 not found response
    ticket = get_object_or_404(Ticket, id=ticket_id)
    user = request.user
    session_key = request.session.session_key or ''

    upvote, created = Upvote.objects.get_or_create(
        user=user if user.is_authenticated else None,
        session_key=session_key if not user.is_authenticated else '',
        ticket=ticket,
        defaults={'vote_weight': 1}  # You can change the vote_weight if needed
    )

    if not created:
        # If the upvote already exists, you may want to either:
        # 1. Do nothing (prevent multiple upvotes), or
        # 2. Toggle the upvote (upvote again to undo).
        # Here, we're assuming we simply ignore the second upvote.
        return JsonResponse({
            'success': False,
            'message': 'You have already upvoted this ticket.',
            'upvote_count': ticket.upvotes.count()  # Sending the current upvote count back
        })

    # Get or create the user's profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    if created:
        # If the profile was just created, the default points are already set in the model
        pass

    # Use the model's method to add points
    profile.add_points(2, 'upvote')

    # Increase the ticket upvotes and save
    ticket.upvotes += 1
    ticket.save()

    # Return a JSON response indicating success
    return JsonResponse({'status': 'success', 'message': 'Thank you for upvoting!', 'upvotes': ticket.upvotes, 'upvote_count': ticket.upvotes.count()})


def profile(request):
    # user = Profile.objects.get()
    return render(request, 'profile.html')


def leaderboard(request):
    leaderboard_users = Profile.objects.order_by('-points')[:10]  # Get top 10 users
    return render(request, 'leaderboard.html', {'leaderboard_users': leaderboard_users})
