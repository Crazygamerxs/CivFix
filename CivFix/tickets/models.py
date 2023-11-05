from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    CATEGORY_CHOICES = [
        ('INFRASTRUCTURE', 'Infrastructure'),
        ('SAFETY_SECURITY', 'Safety & Security'),
        ('SANITATION_HEALTH', 'Sanitation & Health'),
        ('TRAFFIC_TRANSPORTATION', 'Traffic & Transportation'),
    ]

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='INFRASTRUCTURE')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE, default='admin')

    def __str__(self):
        return self.title

    def calculate_total_upvote(self):
        pass
        # return self.upvote_set.count()

class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ticket = models.ForeignKey(Ticket, related_name='upvotes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    vote_weight = models.IntegerField(default=1)

    class Meta:
        unique_together = [('user', 'ticket'), ('session_key', 'ticket')]
        index_together = [['user', 'ticket'], ['session_key', 'ticket']]

    def __str__(self):
        username = self.user.username if self.user else 'Anonymous'
        return f"{username} upvoted {self.ticket.title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def add_points(self, points):
        self.points += points
        self.save()

    def __str__(self):
        return self.user.username
