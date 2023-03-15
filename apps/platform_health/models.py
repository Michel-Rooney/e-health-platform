from apps.arduino.models import HeartRateData
from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    LEVELS = (
        ('A', 'Admin'),
        ('D', 'Doctor'),
        ('P', 'Patients')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=256)
    level = models.CharField(max_length=1, choices=LEVELS, default='P')
    phone_number = models.CharField(max_length=19, unique=True)
    address = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_picture') 

    def __str__(self) -> str:
        return f'{self.user.username} | {self.level}'
    

class Note(models.Model):
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    note = models.TextField()
    date = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.person.user.username} | notes'


class PersonData(models.Model):
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, blank=True)
    beats = models.ManyToManyField(HeartRateData, related_name="beats", blank=True)
    notes = models.ManyToManyField(Note, blank=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    date = models.DateTimeField()

    def __str__(self) -> str:
        return self.person.user.username
    

class Doctor(models.Model):
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    patients = models.ManyToManyField(PersonData, related_name='patients', blank=True)

    def __str__(self) -> str:
        return f'{self.person.user.username} | Doctor'