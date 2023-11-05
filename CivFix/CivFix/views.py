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
