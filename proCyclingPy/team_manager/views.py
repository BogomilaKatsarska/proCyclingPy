from django.shortcuts import render
from django.views.generic import UpdateView

from proCyclingPy.team_manager.forms import TeamManagerEditForm
from proCyclingPy.team_manager.models import TeamManager


class EditTeamManager(UpdateView):
    model = TeamManager
    template_name = 'team-manager/edit-profile.html'
    form_class = TeamManagerEditForm
    # success_url = reverse_lazy()