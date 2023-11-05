from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


#def profile(request, username):
#     user = UserProfile.objects.get(user__username=username)
#     return render(request, 'profile.html', {'user': user})


# def leaderboard(request):
#     leaderboard_users = UserProfile.objects.order_by('-points')[:10]  # Get top 10 users
#     return render(request, 'leaderboard.html', {'leaderboard_users': leaderboard_users})

#from django.shortcuts import render, redirect
# from .models import Ticket
# from .forms import TicketForm

# def home(request):
#     if request.method == 'POST':
#         # Assuming the form data comes via POST request
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to the same page to display the form again
#             return redirect('tickets:home')
#     else:
#         form = TicketForm()

#     # Fetch tickets to display them
#     tickets = Ticket.objects.all()
#     return render(request, 'tickets/home.html', {'form': form, 'tickets': tickets})
