from django.shortcuts import render
from django.views.generic import UpdateView, DetailView, DeleteView

from proCyclingPy.team_manager.forms import TeamManagerEditForm, TeamManagerViewForm
from proCyclingPy.team_manager.models import TeamManager


class EditTeamManager(UpdateView):
    model = TeamManager
    template_name = 'team-manager/edit-profile.html'
    form_class = TeamManagerEditForm
    # success_url = reverse_lazy()


class ViewTeamManagerView(DetailView):
    model = TeamManager
    # form_class = TeamManagerViewForm
    template_name = 'team-manager/details-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.user.pk
        context['pk'] = pk
        return context


class DeleteTeamManager(DeleteView):
    model = TeamManager
    template_name = 'team-manager/delete-profile.html'
    # success_url = reverse_lazy('deleted success')

    def get_object(self, queryset=None):
        return self.request.user