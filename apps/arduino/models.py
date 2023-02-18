from django.contrib.auth.models import User
from django.db import models


class Beats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beats = models.IntegerField()

    def __str__(self):
        return self.user.username