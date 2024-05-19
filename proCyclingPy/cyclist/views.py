from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from proCyclingPy.cyclist.forms import CyclistEditForm
from proCyclingPy.cyclist.models import Cyclist


class EditCyclist(UpdateView):
    model = Cyclist
    template_name = 'cyclist/edit-profile.html'
    form_class = CyclistEditForm
    # success_url = reverse_lazy()