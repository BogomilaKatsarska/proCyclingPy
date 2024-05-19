from django.contrib import admin
from proCyclingPy.common.models import Team, Job


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
