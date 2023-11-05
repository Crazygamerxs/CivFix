from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

def home(request):
    if request.method == 'POST':
        # Assuming the form data comes via POST request
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the same page to display the form again
            return redirect('tickets:home')
    else:
        form = TicketForm()

    # Fetch tickets to display them
    tickets = Ticket.objects.all()
    return render(request, 'tickets/home.html', {'form': form, 'tickets': tickets})
