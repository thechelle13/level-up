from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """Events hosted by gamers."""
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    organizerId = models.ForeignKey(User, on_delete=models.CASCADE)
    gameId = models.ForeignKey("Game", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} on {self.date} at {self.time}"