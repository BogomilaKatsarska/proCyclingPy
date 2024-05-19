from django.contrib import admin

from proCyclingPy.team_manager.models import TeamManager


@admin.register(TeamManager)
class TeamManagerAdmin(admin.ModelAdmin):
    pass