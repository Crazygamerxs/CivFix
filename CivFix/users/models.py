from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def add_points(self, points, reason):
        self.points += points
        self.save()

    def subtract_points(self, points, reason):
        pass

    def __str__(self):
        return self.user.username
