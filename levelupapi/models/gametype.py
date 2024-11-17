from django.db import models


class GameType(models.Model):
    """Game types like board games or card games."""
    label = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.label