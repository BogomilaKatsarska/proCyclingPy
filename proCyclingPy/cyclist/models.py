from datetime import date

from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField

from proCyclingPy.common.models import Team

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
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )
    specialty = models.CharField(
        max_length=SPECIALTY_MAX_LEN,
        choices=SPECIALTIES,
        null=True,
        blank=True,
    )
    country = CountryField()
    weight = models.FloatField(
        null=True,
        blank=True,
    )
    height_in_cm = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        null=True,
        blank=True,
    )
    about = models.TextField(
        max_length=ABOUT_MAX_LEN,
        null=True,
        blank=True,
    )
    employed = models.BooleanField(
        null=True,
        blank=True,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    strava = models.URLField(
        null=True,
        blank=True,
    )
    points = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

        return age

    @property
    def daily_kcal_loose_weight(self):
        return (655 + (9.6 * self.weight) + (1.8 * self.height_in_cm) - (4.7 * self.age)*1.75*1.45) - 300

    @property
    def daily_kcal_maintain_weight(self):
        return 655 + (9.6 * self.weight) + (1.8 * self.height_in_cm) - (4.7 * self.age) * 1.75 * 1.45

    @property
    def get_all_unemployed_cyclists(self):
        return Cyclist.objects.filter(employed=False)