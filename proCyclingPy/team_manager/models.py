from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class TeamManager(models.Model):
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='team_manager',
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
    profile_picture = models.ImageField(
        upload_to='BASE_DIR / team-managers',
        null=True,
        blank=True,
        #TODO: add default
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'