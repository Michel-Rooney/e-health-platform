from django.contrib.auth.models import User
from apps.arduino.models import Beats
from django.db import models


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return f'{self.user.username} | notes'
    

class Person(models.Model):
    LEVELS = (
        ('A', 'Admin'),
        ('D', 'Doctor'),
        ('P', 'Patients')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.ManyToManyField(Note)
    beats = models.ForeignKey(Beats, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    code = models.CharField(max_length=256)
    level = models.CharField(max_length=1, choices=LEVELS, default='P')

    def __str__(self):
        return f'{self.user.username} | {self.level}'