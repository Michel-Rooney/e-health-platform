from django.contrib.auth.models import User
from apps.arduino.models import HeartRateData
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
    code = models.CharField(max_length=256)
    level = models.CharField(max_length=1, choices=LEVELS, default='P')

    def __str__(self):
        return f'{self.user.username} | {self.level}'


class PersonData(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    beats = models.ManyToManyField(HeartRateData, related_name="beats", blank=True)
    notes = models.ManyToManyField(Note, blank=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    phone_number = models.CharField(max_length=19, unique=True)

    def __str__(self):
        return self.phone_number