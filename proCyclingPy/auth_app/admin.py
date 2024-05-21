from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from proCyclingPy.auth_app.models import Profile

UserModel = get_user_model()

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
