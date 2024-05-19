from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from proCyclingPy.auth_app.managers import AppUserManager


class Profile(AbstractBaseUser, PermissionsMixin):
    ROLE_MAX_LEN = 15
    CYCLIST = 'Cyclist'
    TEAM_MANAGER = 'Team Manager'

    ROLES = (
        (CYCLIST, CYCLIST),
        (TEAM_MANAGER, TEAM_MANAGER),
    )

    username = None
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    role = models.CharField(
        max_length=ROLE_MAX_LEN,
        choices=ROLES,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )
    last_login = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = AppUserManager()

    def __str__(self):
        return self.email
