from django.db import models
from django.contrib.auth.models import User

class EventGamer(models.Model):
    """Mapping of users to events they are attending."""
    eventId = models.ForeignKey("Event", on_delete=models.CASCADE)
    gamerId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.gamerId.username} attending {self.eventId.description}"