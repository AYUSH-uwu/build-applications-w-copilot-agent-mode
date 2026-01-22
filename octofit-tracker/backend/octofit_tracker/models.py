from django.db import models
from djongo import models as djongo_models
from bson import ObjectId

class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey('Team', related_name='members', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey('User', related_name='activities', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    date = models.DateField()

    def __str__(self):
        return f"{self.type} by {self.user.name} on {self.date}"

class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.ManyToManyField('Team', related_name='workouts', blank=True)

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey('User', related_name='leaderboard_entries', on_delete=models.CASCADE)
    score = models.IntegerField()
    rank = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.name} - Rank {self.rank}"
