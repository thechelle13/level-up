from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """Games that users create."""
    title = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    skill_level = models.IntegerField()
    number_of_players = models.IntegerField()
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    gamer = models.ForeignKey(User, on_delete=models.CASCADE)
