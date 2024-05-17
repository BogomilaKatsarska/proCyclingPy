from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField

UserModel = get_user_model()


class Cyclist(models.Model):
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20
    ABOUT_MAX_LEN = 1000
    SPECIALTY_MAX_LEN = 50

    ONE_DAY_RACES = 'One Day Races'
    GC = 'General Classification'
    TT = 'Time Trail'
    SPRINT = 'Sprint'
    CLIMBER = 'Climber'
    HILLS = 'Hills'

    SPECIALTIES = (
        (ONE_DAY_RACES, ONE_DAY_RACES),
        (GC, GC),
        (TT, TT),
        (SPRINT, SPRINT),
        (CLIMBER, CLIMBER),
        (HILLS, HILLS),
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=False,
        blank=False,
    )
    specialty = models.CharField(
        max_length=SPECIALTY_MAX_LEN,
        choices=SPECIALTIES,
        null=False,
        blank=False,
    )
    country = CountryField()
    weight = models.FloatField(
        null=False,
        blank=False,
    )
    height = models.FloatField(
        null=False,
        blank=False,
    )
    about = models.TextField(
        max_length=ABOUT_MAX_LEN,
    )
    strava = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
