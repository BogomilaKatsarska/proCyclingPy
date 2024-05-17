from django.contrib import admin

from proCyclingPy.cyclist.models import Cyclist


@admin.register(Cyclist)
class CyclistAdmin(admin.ModelAdmin):
    pass