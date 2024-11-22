from django.db import models
from django.contrib.auth.models import User

class Gamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user.username