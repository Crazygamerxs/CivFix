from django.db.models import Sum
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
        defaults={'vote_weight': 1}
    )

    if not created:
        # simply ignore the second upvote
        return JsonResponse({
            'success': False,
            'message': 'You have already upvoted this ticket.',
            'upvote_count': ticket.upvotes.count()  # Sending the current upvote count back
        })

    # Get or create the user's profile
    creator_profile, profile_created = Profile.objects.get_or_create(user=ticket.creator)

    if created:
        pass

    # Use the model's method to add points
    creator_profile.add_points(2)

    # Increase the ticket upvotes and save
    upvote_count = ticket.upvotes.count()

    # return render(request, 'home.html')
    # Return a JSON response indicating success
    return JsonResponse({
        'status': 'success',
        'message': 'Thank you for upvoting!',
        'upvote_count': upvote_count
    })


def profile(request):
    query = request.GET.get('username', '') # Gets the username query from the request
    if query:
        user = User.objects.filter(username__iexact=query).first() # Find the user by username
        if user:
            profile = Profile.objects.get(user=user)
            # Your logic to gather additional data for the user profile goes here
            # ...
            context = {'profile': profile}
            return render(request, 'profile.html', context)
        else:
            # User not found, render some error or a blank profile template
            return render(request, 'profile.html', {'error': 'User not found'})
    else:
        # Default profile page when no search query is present
        # You can also handle this to show the profile of the logged-in user or some default content
        return render(request, 'profile.html')


def leaderboard(request):
    leaderboard_users = Profile.objects.order_by('-points')[:10]  # Get top 10 users
    return render(request, 'leaderboard.html', {'leaderboard_users': leaderboard_users})
