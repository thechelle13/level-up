from django.db import models
from django.contrib.auth.models import User

class EventGamer(models.Model):
    """Mapping of users to events they are attending."""
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    gamer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.gamer.username} attending {self.event.description}"
    
    
    
    
#     from django.db import models
# from django.contrib.auth.models import User


# class EventGamer(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="signed_up_events"
#     )
#     event = models.ForeignKey(
#         "Event", on_delete=models.CASCADE, related_name="participants")