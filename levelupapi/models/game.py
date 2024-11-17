from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    """Games that users create."""
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    maker = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    skill_level = models.CharField(max_length=50)
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title