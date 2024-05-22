from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView

from proCyclingPy.cyclist.forms import CyclistEditForm, CyclistViewForm
from proCyclingPy.cyclist.models import Cyclist


class EditCyclistView(UpdateView):
    model = Cyclist
    template_name = 'cyclist/edit-profile.html'
    form_class = CyclistEditForm
    # success_url = reverse_lazy()


class CyclistListView(ListView):
    model = Cyclist
    template_name = 'cyclist/cyclists.html'
    paginate_by = 9




class ViewCyclistView(DetailView):
    model = Cyclist
    form_class = CyclistViewForm
    template_name = 'cyclist/details-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.user.pk
        context['pk'] = pk
        return context
