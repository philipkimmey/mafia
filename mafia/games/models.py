from django.db import models

from django.contrib.auth.models import User


class Game(models.Model):
    current_round = models.ForeignKey('games.Round')
    max_participants = models.IntegerField(default=8)


ROLE_CHOICES = (
        ('villager', 'Villager'),
        ('mafioso', 'Mafioso'),
        ('angel', 'Angel'),
        ('detective', 'Detective'),
)


class UserGame(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    role = models.CharField(max_length=10,
            choices=ROLE_CHOICES)


PHASE_CHOICES = (
        ('night', 'Nighttime'),
        ('day', 'Daytime'),
)


class Round(models.Model):
    number = models.IntegerField(default=1)
    phase = models.CharField(max_length=10,
            choices=PHASE_CHOICES)


class Vote(models.Model):
    round = models.ForeignKey(Round)
    voter = models.ForeignKey(User)
    target = models.ForeignKey(User)

    class Meta:
        unique_together = (('round', 'voter'))
